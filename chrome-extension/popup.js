// Popup management script
let playlist = [];
let currentVideoIndex = 0;
let settings = {
    videoQuality: '480',
    downloadPath: 'Downloads/Karaoke'
};

// DOM Elements
const youtubeUrlInput = document.getElementById('youtube-url');
const addVideoBtn = document.getElementById('add-video');
const playAllBtn = document.getElementById('play-all');
const clearPlaylistBtn = document.getElementById('clear-playlist');
const playlistDiv = document.getElementById('playlist');
const statusDiv = document.getElementById('status');
const videoQualitySelect = document.getElementById('video-quality');
const downloadPathInput = document.getElementById('download-path');
const saveSettingsBtn = document.getElementById('save-settings');

// Load playlist and settings from storage on startup
chrome.storage.local.get(['playlist', 'settings'], (result) => {
    if (result.playlist) {
        playlist = result.playlist;
        updatePlaylistUI();
    }
    if (result.settings) {
        settings = result.settings;
        // Update UI with loaded settings
        videoQualitySelect.value = settings.videoQuality;
        downloadPathInput.value = settings.downloadPath;
    }
});

// Save settings
saveSettingsBtn.addEventListener('click', async () => {
    settings.videoQuality = videoQualitySelect.value;
    settings.downloadPath = downloadPathInput.value.trim() || 'Downloads/Karaoke';
    
    await saveSettings();
    showStatus('Impostazioni salvate', 'success');
});

// Add video to playlist
addVideoBtn.addEventListener('click', async () => {
    const url = youtubeUrlInput.value.trim();
    
    if (!url) {
        showStatus('Inserisci un link YouTube valido', 'error');
        return;
    }
    
    // Validate YouTube URL
    if (!isValidYouTubeUrl(url)) {
        showStatus('URL YouTube non valido', 'error');
        return;
    }
    
    // Extract video ID
    const videoId = extractVideoId(url);
    if (!videoId) {
        showStatus('Impossibile estrarre l\'ID del video', 'error');
        return;
    }
    
    // Check if video already in playlist
    if (playlist.some(v => v.id === videoId)) {
        showStatus('Video già nella playlist', 'error');
        return;
    }
    
    // Add to playlist
    const video = {
        id: videoId,
        url: url,
        title: `Video YouTube (${videoId})`,
        status: 'pending',
        downloadPath: null
    };
    
    playlist.push(video);
    await savePlaylist();
    updatePlaylistUI();
    youtubeUrlInput.value = '';
    showStatus('Video aggiunto alla playlist', 'success');
});

// Play all videos
playAllBtn.addEventListener('click', async () => {
    if (playlist.length === 0) {
        showStatus('Playlist vuota', 'error');
        return;
    }
    
    showStatus('Avvio riproduzione playlist...', 'info');
    
    // Send message to background script to start playback
    chrome.runtime.sendMessage({
        action: 'playPlaylist',
        playlist: playlist,
        settings: settings
    }, (response) => {
        if (response && response.success) {
            showStatus('Riproduzione avviata', 'success');
        } else {
            showStatus('Errore nell\'avviare la riproduzione: ' + (response?.error || 'unknown'), 'error');
        }
    });
});

// Clear playlist
clearPlaylistBtn.addEventListener('click', async () => {
    if (confirm('Vuoi davvero cancellare tutta la playlist?')) {
        playlist = [];
        await savePlaylist();
        updatePlaylistUI();
        showStatus('Playlist cancellata', 'info');
    }
});

// Remove single video from playlist
async function removeVideo(index) {
    playlist.splice(index, 1);
    await savePlaylist();
    updatePlaylistUI();
    showStatus('Video rimosso', 'info');
}

// Update playlist UI
function updatePlaylistUI() {
    if (playlist.length === 0) {
        playlistDiv.innerHTML = '<p class="empty-message">Nessun video in playlist</p>';
        playAllBtn.disabled = true;
        clearPlaylistBtn.disabled = true;
        return;
    }
    
    playAllBtn.disabled = false;
    clearPlaylistBtn.disabled = false;
    
    playlistDiv.innerHTML = playlist.map((video, index) => `
        <div class="playlist-item">
            <div class="video-info">
                <span class="video-title">${video.title}</span>
                <span class="video-status ${video.status}">${getStatusText(video.status)}</span>
            </div>
            <button class="remove-btn" data-index="${index}">✖</button>
        </div>
    `).join('');
    
    // Add event listeners to remove buttons
    playlistDiv.querySelectorAll('.remove-btn').forEach(btn => {
        btn.addEventListener('click', (e) => {
            const index = parseInt(e.target.dataset.index);
            removeVideo(index);
        });
    });
}

// Get status text in Italian
function getStatusText(status) {
    const statusMap = {
        'pending': 'In attesa',
        'downloading': 'Download...',
        'ready': 'Pronto',
        'playing': 'In riproduzione',
        'played': 'Riprodotto',
        'error': 'Errore'
    };
    return statusMap[status] || status;
}

// Save playlist to storage
async function savePlaylist() {
    return new Promise((resolve) => {
        chrome.storage.local.set({ playlist: playlist }, () => {
            resolve();
        });
    });
}

// Save settings to storage
async function saveSettings() {
    return new Promise((resolve) => {
        chrome.storage.local.set({ settings: settings }, () => {
            resolve();
        });
    });
}

// Show status message
function showStatus(message, type = 'info') {
    statusDiv.textContent = message;
    statusDiv.className = `status show ${type}`;
    
    setTimeout(() => {
        statusDiv.classList.remove('show');
    }, 5000);
}

// Validate YouTube URL
function isValidYouTubeUrl(url) {
    const patterns = [
        /^(https?:\/\/)?(www\.)?(youtube\.com\/watch\?v=)[\w-]+/,
        /^(https?:\/\/)?(www\.)?(youtu\.be\/)[\w-]+/,
        /^(https?:\/\/)?(www\.)?(youtube\.com\/embed\/)[\w-]+/
    ];
    
    return patterns.some(pattern => pattern.test(url));
}

// Extract video ID from YouTube URL
function extractVideoId(url) {
    const patterns = [
        /[?&]v=([\w-]{11})/,  // youtube.com/watch?v=... (11 chars: letters, numbers, hyphens, underscores)
        /youtu\.be\/([\w-]{11})/,  // youtu.be/... (11 chars)
        /embed\/([\w-]{11})/  // youtube.com/embed/... (11 chars)
    ];
    
    for (const pattern of patterns) {
        const match = url.match(pattern);
        if (match && match[1].length === 11) {
            return match[1];
        }
    }
    
    return null;
}

// Listen for messages from background script
chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
    if (message.action === 'updateVideoStatus') {
        const video = playlist.find(v => v.id === message.videoId);
        if (video) {
            video.status = message.status;
            if (message.downloadPath) {
                video.downloadPath = message.downloadPath;
            }
            savePlaylist();
            updatePlaylistUI();
        }
    } else if (message.action === 'playbackComplete') {
        showStatus('Riproduzione completata', 'success');
        // Reload playlist to show updated status
        chrome.storage.local.get(['playlist'], (result) => {
            if (result.playlist) {
                playlist = result.playlist;
                updatePlaylistUI();
            }
        });
    }
});

// Allow pressing Enter to add video
youtubeUrlInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') {
        addVideoBtn.click();
    }
});
