<script>
    // Update date and time
    function updateDateTime() {
        const now = new Date();
        const options = { 
            weekday: 'long', 
            year: 'numeric', 
            month: 'long', 
            day: 'numeric',
            hour: '2-digit',
            minute: '2-digit'
        };
        document.getElementById('currentDateTime').textContent = now.toLocaleDateString('en-IN', options);
    }
    
    updateDateTime();
    setInterval(updateDateTime, 60000);
    
    // Simulate view counts (would be replaced with real data in production)
    document.querySelectorAll('.card-meta span:last-child').forEach(el => {
        const views = parseInt(el.textContent.replace(/,/g, ''));
        setInterval(() => {
            const increment = Math.floor(Math.random() * 10);
            const newViews = views + increment;
            el.textContent = newViews.toLocaleString() + ' views';
        }, 5000);
    });
</script>
