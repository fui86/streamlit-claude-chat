// Background script for Firefox extension
// Firefox doesn't have chrome.system.display API, so we use browser.windows instead

let currentPlayingVideo = null;
let playerWindowId = null;
let isPlaybackActive = false;

// Use browser API for Firefox compatibility
const browserAPI = typeof browser !== 'undefined' ? browser : chrome;

// Listen for messages from popup
browserAPI.runtime.onMessage.addListener((message, sender, sendResponse) => {
    if (message.action === 'playPlaylist') {
        handlePlayPlaylist(message.playlist, message.settings)
            .then(() => sendResponse({ success: true }))
            .catch((error) => sendResponse({ success: false, error: error.message }));
        return true; // Keep message channel open for async response
    }
});

// Handle playlist playback
async function handlePlayPlaylist(playlist, settings = {}) {
    if (isPlaybackActive) {
        throw new Error('Una riproduzione è già in corso');
    }
    
    if (!playlist || playlist.length === 0) {
        throw new Error('Playlist vuota');
    }
    
    // Set default settings if not provided
    const defaultSettings = {
        videoQuality: '480',
        downloadPath: 'Downloads/Karaoke'
    };
    const playbackSettings = { ...defaultSettings, ...settings };
    
    isPlaybackActive = true;
    
    try {
        // Get all displays to find secondary monitor
        // Firefox doesn't have system.display, so we'll use a simpler approach
        const displays = await getDisplays();
        
        // Play each video in sequence
        for (let i = 0; i < playlist.length; i++) {
            const video = playlist[i];
            await playVideo(video, displays, playbackSettings);
        }
        
        // Notify popup that playback is complete
        browserAPI.runtime.sendMessage({
            action: 'playbackComplete'
        });
        
    } finally {
        isPlaybackActive = false;
    }
}

// Get display information (Firefox-compatible)
async function getDisplays() {
    // Firefox doesn't have chrome.system.display
    // We'll create a mock display structure
    // In Firefox, we can't detect multiple monitors directly from the extension
    // So we'll just return a single display and let the user position the window
    return [
        {
            bounds: {
                left: 0,
                top: 0,
                width: 1920,
                height: 1080
            }
        }
    ];
}

// Play a single video
async function playVideo(video, displays, settings) {
    try {
        // Update status to downloading
        updateVideoStatus(video.id, 'downloading');
        
        // Note: Direct YouTube download requires external services/APIs
        // This implementation uses YouTube embed for playback
        
        // Determine target display (prefer secondary monitor)
        let targetDisplay = displays[0];
        if (displays.length > 1) {
            // Use second display if available
            targetDisplay = displays[1];
        }
        
        // Calculate window position for fullscreen on target display
        const windowOptions = {
            url: browserAPI.runtime.getURL(`player.html?videoId=${encodeURIComponent(video.id)}&quality=${encodeURIComponent(settings.videoQuality)}&path=${encodeURIComponent(settings.downloadPath)}`),
            type: 'popup',
            // Firefox uses 'fullscreen' state differently
            state: 'maximized',
            left: targetDisplay.bounds.left,
            top: targetDisplay.bounds.top,
            width: targetDisplay.bounds.width,
            height: targetDisplay.bounds.height
        };
        
        // Update status to ready
        updateVideoStatus(video.id, 'ready');
        
        // Open player window
        const window = await browserAPI.windows.create(windowOptions);
        playerWindowId = window.id;
        currentPlayingVideo = video;
        
        // Update status to playing
        updateVideoStatus(video.id, 'playing');
        
        // Wait for video to finish (user will close the window)
        await waitForWindowClose(window.id);
        
        // After video finishes, ask user if they want to delete
        await promptDeleteFile(video);
        
        // Update status to played
        updateVideoStatus(video.id, 'played');
        
    } catch (error) {
        console.error('Error playing video:', error);
        updateVideoStatus(video.id, 'error');
        throw error;
    }
}

// Wait for window to be closed
function waitForWindowClose(windowId) {
    return new Promise((resolve) => {
        const checkInterval = setInterval(async () => {
            try {
                await browserAPI.windows.get(windowId);
            } catch (error) {
                // Window is closed
                clearInterval(checkInterval);
                resolve();
            }
        }, 500);
    });
}

// Prompt user to delete downloaded file after playback
async function promptDeleteFile(video) {
    // Create a dialog window for the deletion prompt
    // This allows user to choose whether to keep or delete the video file
    
    // Create a new window for the deletion prompt
    const promptWindow = await browserAPI.windows.create({
        url: browserAPI.runtime.getURL(`delete-prompt.html?videoId=${video.id}`),
        type: 'popup',
        width: 400,
        height: 200
    });
    
    // Wait for user response
    return new Promise((resolve) => {
        const listener = (message, sender) => {
            if (message.action === 'deleteResponse' && message.videoId === video.id) {
                browserAPI.runtime.onMessage.removeListener(listener);
                resolve(message.shouldDelete);
            }
        };
        browserAPI.runtime.onMessage.addListener(listener);
    });
}

// Update video status
function updateVideoStatus(videoId, status, downloadPath = null) {
    browserAPI.runtime.sendMessage({
        action: 'updateVideoStatus',
        videoId: videoId,
        status: status,
        downloadPath: downloadPath
    });
}

// Handle extension installation
browserAPI.runtime.onInstalled.addListener(() => {
    console.log('Karaoke Video Player extension installed');
});

// Clean up when window is closed
browserAPI.windows.onRemoved.addListener((windowId) => {
    if (windowId === playerWindowId) {
        playerWindowId = null;
    }
});
