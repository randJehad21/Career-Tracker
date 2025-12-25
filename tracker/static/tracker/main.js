document.addEventListener("DOMContentLoaded", () => {

    // Map status codes to CSS classes
    const statusMap = {
        "AP": "applied",
        "IN": "interview",
        "OF": "offer",
        "RJ": "rejected"
    };

    // Function to update the select element's color
    function updateSelectColor(select) {
        // Remove previous status classes
        select.classList.remove("status-applied", "status-interview", "status-offer", "status-rejected");
        // Add new class based on current value
        const code = select.value;
        select.classList.add("status-" + statusMap[code]);
    }

    // STATUS UPDATE + color on page load
    document.querySelectorAll(".status-select").forEach(select => {

        // Initialize color on page load
        updateSelectColor(select);

        // Handle change event
        select.addEventListener("change", function () {
            const appId = this.dataset.id;
            const status = this.value;

            // Update color immediately
            updateSelectColor(this);

            // AJAX POST to update status in backend
            fetch(`/update-status/${appId}/`, {
                method: "POST",
                headers: {
                    "X-CSRFToken": getCookie("csrftoken"),
                    "Content-Type": "application/x-www-form-urlencoded"
                },
                body: `status=${encodeURIComponent(status)}`
            })
            .then(response => response.json())
            .then(result => {
                if (!result.success) {
                    alert("Error updating status");
                }
            });
        });
    });

    // DELETE APPLICATION
    document.querySelectorAll(".delete-btn").forEach(button => {
        button.addEventListener("click", function () {
            const appId = this.dataset.id;

            if (!confirm("Are you sure you want to delete this application?")) return;

            fetch(`/delete-ajax/${appId}/`, {
                method: "POST",
                headers: {
                    "X-CSRFToken": getCookie("csrftoken"),
                    "Content-Type": "application/x-www-form-urlencoded"
                },
            })
            .then(response => response.json())
            .then(result => {
                if (result.success) {
                    const row = document.getElementById(`row-${appId}`);
                    if (row) row.remove();
                } else {
                    alert("Error deleting application");
                }
            });
        });
    });
});

// ✅ CSRF helper
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let cookie of cookies) {
            cookie = cookie.trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


// FILTER BY STATUS
const statusFilter = document.getElementById('status-filter');
if (statusFilter) {
    statusFilter.addEventListener('change', function() {
        const selected = this.value; // 'AP', 'IN', 'OF', 'RJ', or 'all'
        document.querySelectorAll('tbody tr').forEach(row => {
            const select = row.querySelector('.status-select');
            if (!select) return;
            if (selected === 'all' || select.value === selected) {
                row.style.display = '';
            } else {
                row.style.display = 'none';
            }
        });
    });
}

// LIVE SEARCH
const searchInput = document.getElementById('search-input');
if (searchInput) {
    searchInput.addEventListener('input', function() {
        const query = this.value.toLowerCase();
        document.querySelectorAll('tbody tr').forEach(row => {
            const company = row.querySelector('td[data-label="Company"]').textContent.toLowerCase();
            const position = row.querySelector('td[data-label="Position"]').textContent.toLowerCase();
            if (company.includes(query) || position.includes(query)) {
                row.style.display = '';
            } else {
                row.style.display = 'none';
            }
        });
    });
}
