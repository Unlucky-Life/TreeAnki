document.addEventListener('keydown', function(event) {
// Check if the '8' key was pressed
if (event.key === '8') {
    toggleTreFame();
}
});

function toggleTreFame() {
const iframe = document.querySelector('.TreFame');
// Toggle display between 'block' and 'none'
iframe.style.display = (iframe.style.display === 'none' || iframe.style.display === '') ? 'block' : 'none';
}