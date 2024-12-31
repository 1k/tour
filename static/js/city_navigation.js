document.addEventListener('DOMContentLoaded', function() {
    // 城市导航平滑滚动并定位到城市标题
    document.querySelectorAll('.nav-link').forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            const cityId = this.getAttribute('href').substring(1);
            const citySection = document.getElementById(cityId);
            
            if (citySection) {
                const cityHeader = citySection.querySelector('.city-header');
                
                // 平滑滚动到城市标题，并略微偏移，使标题不贴近顶部
                window.scrollTo({
                    top: cityHeader.getBoundingClientRect().top + window.pageYOffset - 80, // 减去导航栏高度
                    behavior: 'smooth'
                });

                // 短暂高亮城市标题
                cityHeader.style.transition = 'background-color 0.5s';
                cityHeader.style.backgroundColor = 'rgba(44, 125, 160, 0.1)';
                setTimeout(() => {
                    cityHeader.style.backgroundColor = '';
                }, 1000);
            }
        });
    });
});
