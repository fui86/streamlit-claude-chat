// Player script
let videoId = null;

// Get video ID from URL parameters
function init() {
    const urlParams = new URLSearchParams(window.location.search);
    videoId = urlParams.get('videoId');
    
    if (!videoId) {
        showError('ID video mancante');
        return;
    }
    
    loadVideo(videoId);
}

// Load video
function loadVideo(id) {
    const videoContainer = document.getElementById('video-container');
    const videoPlayer = document.getElementById('video-player');
    const loading = document.getElementById('loading');
    const videoTitle = document.getElementById('video-title');
    
    // Set YouTube embed URL with autoplay and controls
    const embedUrl = `https://www.youtube.com/embed/${id}?autoplay=1&controls=1&rel=0&modestbranding=1`;
    
    videoPlayer.src = embedUrl;
    videoTitle.textContent = `Video: ${id}`;
    
    // Show video container and hide loading after a delay
    setTimeout(() => {
        loading.style.display = 'none';
        videoContainer.style.display = 'flex';
        
        // Try to enter fullscreen
        enterFullscreen();
    }, 1000);
}

// Enter fullscreen mode
function enterFullscreen() {
    const elem = document.documentElement;
    
    if (elem.requestFullscreen) {
        elem.requestFullscreen().catch(err => {
            console.log('Fullscreen error:', err);
        });
    } else if (elem.webkitRequestFullscreen) { // Safari
        elem.webkitRequestFullscreen();
    } else if (elem.msRequestFullscreen) { // IE11
        elem.msRequestFullscreen();
    }
}

// Toggle fullscreen
function toggleFullscreen() {
    if (!document.fullscreenElement && 
        !document.webkitFullscreenElement && 
        !document.msFullscreenElement) {
        enterFullscreen();
    } else {
        exitFullscreen();
    }
}

// Exit fullscreen
function exitFullscreen() {
    if (document.exitFullscreen) {
        document.exitFullscreen();
    } else if (document.webkitExitFullscreen) {
        document.webkitExitFullscreen();
    } else if (document.msExitFullscreen) {
        document.msExitFullscreen();
    }
}

// Show error
function showError(message) {
    const loading = document.getElementById('loading');
    const error = document.getElementById('error');
    const errorMessage = document.getElementById('error-message');
    
    loading.style.display = 'none';
    error.style.display = 'block';
    errorMessage.textContent = message;
}

// Handle keyboard shortcuts
document.addEventListener('keydown', (e) => {
    // F11 for fullscreen
    if (e.key === 'F11') {
        e.preventDefault();
        toggleFullscreen();
    }
    
    // ESC to close (if not in fullscreen)
    if (e.key === 'Escape' && !document.fullscreenElement) {
        window.close();
    }
});

// Initialize on page load
window.addEventListener('load', init);

// Handle fullscreen change
document.addEventListener('fullscreenchange', () => {
    if (!document.fullscreenElement) {
        console.log('Exited fullscreen');
    }
});
