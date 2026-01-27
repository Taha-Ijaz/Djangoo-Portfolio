// Smooth scroll and animation on load
document.addEventListener('DOMContentLoaded', function() {
    // Animate cards on scroll
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, observerOptions);

    // Observe all cards
    const cards = document.querySelectorAll('.card');
    cards.forEach(card => {
        card.style.opacity = '0';
        card.style.transform = 'translateY(20px)';
        card.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
        observer.observe(card);
    });

    // Add hover effect to contact items
    const contactItems = document.querySelectorAll('.contact-item');
    contactItems.forEach(item => {
        item.addEventListener('mouseenter', function() {
            this.style.color = '#d4af37';
            this.style.transform = 'translateX(5px)';
        });
        
        item.addEventListener('mouseleave', function() {
            this.style.color = '#d0d0d0';
            this.style.transform = 'translateX(0)';
        });
        
        item.style.transition = 'all 0.3s ease';
    });

    // Add click handlers for contact links
    const linkedinItem = contactItems[2];
    const githubItem = contactItems[3];
    
    if (linkedinItem) {
        linkedinItem.style.cursor = 'pointer';
        linkedinItem.addEventListener('click', function() {
            window.open('https://linkedin.com/in/ayesha-fakhar', '_blank');
        });
    }
    
    if (githubItem) {
        githubItem.style.cursor = 'pointer';
        githubItem.addEventListener('click', function() {
            window.open('https://github.com/ayeshafakhar', '_blank');
        });
    }

    // Email click handler
    const emailItem = contactItems[0];
    if (emailItem) {
        emailItem.style.cursor = 'pointer';
        emailItem.addEventListener('click', function() {
            window.location.href = 'mailto:ayesha.fakhar@email.com';
        });
    }

    // Phone click handler
    const phoneItem = contactItems[1];
    if (phoneItem) {
        phoneItem.style.cursor = 'pointer';
        phoneItem.addEventListener('click', function() {
            window.location.href = 'tel:+92XXXXXXXXXX';
        });
    }
});