function showImage(imgElement) {
    var modal = document.getElementById("imageModal");
    var modalImg = document.getElementById("largeImage");

    // Set the source of the modal image
    modalImg.src = imgElement.src;

    // Display the modal
    modal.style.display = "flex";
}

function closeImage() {
    document.getElementById("imageModal").style.display = "none";
}












$(document).ready(function () {
    $(".add").click(function (e) {
        e.preventDefault();
        var productId = $(this).data("id");

        $.ajax({
            url: "/add/" + productId + "/",  // Update with your actual URL
            type: "GET",
            success: function (response) {
                $("#cart-count").text(response.count); // Update the cart count dynamically
                alert("Item added to cart!");
            },
            error: function (error) {
                console.log(error);
            }
        });
    });

    $(".reduce").click(function (e) {
        e.preventDefault();
        var productId = $(this).data("id");

        $.ajax({
            url: "/reduce/" + productId + "/",
            type: "GET",
            success: function (response) {
                $("#cart-items").html(response.html); // Update cart items dynamically
            },
            error: function (error) {
                console.log(error);
            }
        });
    });
});
