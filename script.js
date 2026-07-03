document.addEventListener('DOMContentLoaded', () => {
    const input = document.getElementById("searcher");
    const champions = document.querySelectorAll(".champion-item");
    const items = document.querySelectorAll('.champion-item');

    const modal = document.getElementById('champion-modal');
    const modalContent = document.querySelector('.modal-content');
    const modalName = document.getElementById('modal-name');
    const modalDesc = document.getElementById('modal-desc');
    const modalImg = document.getElementById('modal-img');
    const closeBtn = document.getElementById('close-modal');

    function filterChampions () {
        champions.forEach(listElement => {
            if (listElement.dataset.name.toLowerCase().includes(input.value.toLowerCase())) {
                listElement.style.display = "block";
            } else {
                listElement.style.display = "none";
            }
        })
    }

    items.forEach(item => {
        item.addEventListener('click', () => {
            const name = item.getAttribute('data-name');
            const desc = item.getAttribute('data-desc');
            const img = item.getAttribute('data-img');

            modalName.innerText = name;
            modalDesc.innerHTML = desc;
            modalImg.src = img;
            modalImg.alt = name;

            modalContent.style.setProperty('--bg-image', `url('${img}')`);

            modal.classList.add('active');
        });
    });

    closeBtn.addEventListener('click', () => {
        modal.classList.remove('active');
    });

    window.addEventListener('click', (e) => {
        if (e.target === modal) {
            modal.classList.remove('active');
        }
    });

    input.addEventListener("input", filterChampions);
});