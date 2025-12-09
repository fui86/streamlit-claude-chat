// Delete prompt script
let videoId = null;

// Initialize
function init() {
    const urlParams = new URLSearchParams(window.location.search);
    videoId = urlParams.get('videoId');
    
    if (videoId) {
        document.getElementById('video-info').textContent = `Video ID: ${videoId}`;
    }
    
    // Add event listeners
    document.getElementById('btn-keep').addEventListener('click', () => {
        handleResponse(false);
    });
    
    document.getElementById('btn-delete').addEventListener('click', () => {
        handleResponse(true);
    });
}

// Handle user response
function handleResponse(shouldDelete) {
    // Send response to background script
    chrome.runtime.sendMessage({
        action: 'deleteResponse',
        videoId: videoId,
        shouldDelete: shouldDelete
    }, () => {
        // Close this window
        window.close();
    });
}

// Handle keyboard shortcuts
document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
        handleResponse(false);
    } else if (e.key === 'Delete') {
        handleResponse(true);
    }
});

// Initialize on load
window.addEventListener('load', init);
