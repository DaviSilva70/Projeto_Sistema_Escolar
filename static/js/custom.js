// JavaScript Customizado - Sistema de Gestão Escolar

document.addEventListener('DOMContentLoaded', function() {
    // Toggle Sidebar
    const toggleSidebar = document.getElementById('toggle-sidebar');
    const sidebar = document.getElementById('sidebar');

    if (toggleSidebar && sidebar) {
        toggleSidebar.addEventListener('click', function() {
            sidebar.classList.toggle('collapsed');
            sidebar.classList.toggle('show');
        });
    }

    // Fechar sidebar ao clicar fora (mobile)
    document.addEventListener('click', function(event) {
        if (window.innerWidth < 768) {
            if (sidebar && !sidebar.contains(event.target) && !toggleSidebar.contains(event.target)) {
                sidebar.classList.remove('show');
            }
        }
    });

    // Tooltips do Bootstrap
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });

    // Auto-hide alerts após 5 segundos
    const alerts = document.querySelectorAll('.alert-dismissible');
    alerts.forEach(function(alert) {
        setTimeout(function() {
            const bsAlert = new bootstrap.Alert(alert);
            bsAlert.close();
        }, 5000);
    });
});
