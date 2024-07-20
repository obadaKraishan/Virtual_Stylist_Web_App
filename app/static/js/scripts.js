document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('form');
    form.addEventListener('submit', function(event) {
        const checkboxes = form.querySelectorAll('input[type="checkbox"]');
        let isChecked = false;
        checkboxes.forEach(checkbox => {
            if (checkbox.checked) {
                isChecked = true;
            }
        });
        if (!isChecked) {
            event.preventDefault();
            alert('Please select at least one color.');
        }
    });
});
