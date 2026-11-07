
document.addEventListener("DOMContentLoaded", function () {

    // Automatically hide flash messages after 4 seconds
    const flashMessages = document.querySelectorAll(".flash-message");

    flashMessages.forEach(function (message) {
        setTimeout(function () {
            message.style.transition = "opacity 0.5s ease";
            message.style.opacity = "0";

            setTimeout(function () {
                message.remove();
            }, 500);

        }, 4000);
    });

    // Prevent accidental empty shopping-list submissions
    const shoppingForm = document.querySelector(".shopping-add-form");

    if (shoppingForm) {
        shoppingForm.addEventListener("submit", function (event) {
            const ingredient = shoppingForm
                .querySelector('[name="ingredient"]')
                .value.trim();

            if (!ingredient) {
                event.preventDefault();
                alert("Please enter an ingredient.");
            }
        });
    }

    // Confirm before removing favourite recipes
    const favoriteForms = document.querySelectorAll(
        'form[action*="/favorite/"]'
    );

    favoriteForms.forEach(function (form) {
        form.addEventListener("submit", function (event) {
            const button = form.querySelector("button");

            if (button && button.textContent.includes("Remove")) {
                if (!confirm("Remove this recipe from your favourites?")) {
                    event.preventDefault();
                }
            }
        });
    });

});
