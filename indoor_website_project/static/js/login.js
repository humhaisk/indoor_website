
document.addEventListener('DOMContentLoaded', () => {
    const uploadIcon = document.getElementById('uploadIcon');
    const profilePictureInput = document.getElementById('profilePictureInput');
    const profilePicture = document.getElementById('profilePicture');
    const collegeIdPhotoInput = document.getElementById('collegeIdPhoto');
    const fileNameDisplay = document.getElementById('fileName');
    const profileForm = document.getElementById('profileForm');

    if (uploadIcon && profilePictureInput) {
        uploadIcon.addEventListener('click', () => profilePictureInput.click());
    }

    if (profilePicture && profilePictureInput) {
        profilePicture.addEventListener('click', () => profilePictureInput.click());
        profilePictureInput.addEventListener('change', (event) => {
            const file = event.target.files[0];
            if (file) {
                const reader = new FileReader();
                reader.onload = (e) => { profilePicture.src = e.target.result; };
                reader.readAsDataURL(file);
            }
        });
    }

    if (collegeIdPhotoInput && fileNameDisplay) {
        collegeIdPhotoInput.addEventListener('change', function() {
            fileNameDisplay.textContent = this.files.length > 0 ? `File: ${this.files[0].name}` : '';
        });
    }
});