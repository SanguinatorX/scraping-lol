css = """

body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    background-color: #0a0a0c;
    color: #f0e6d2;
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 40px;
    padding: 60px;
    margin: 0;
}

.champion-item {
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 260px;
    cursor: pointer;
    position: relative;
    z-index: 1;
}

.champion-item:hover {
    z-index: 99;
}

hover-tilt::part(container) {
    border-radius: 8px;
}

.champion-img {
    width: 100%;
    border-radius: 8px;
    display: block;
}

.champion-name {
    color: #c8aa6e;
    font-size: 16px;
    margin-top: 15px;
    text-transform: uppercase;
    letter-spacing: 2px;
    font-weight: 600;
    text-align: center;
}

.modal {
    display: none;
    position: fixed;
    z-index: 9999;
    top: 0; left: 0;
    width: 100vw;
    height: 100vh;
    justify-content: center;
    align-items: center;
}

.modal.active {
    display: flex;
}

.modal-content {
    width: 100%;
    height: 100%;
    padding: 60px;
    box-sizing: border-box;
    position: relative;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;

    background-image: linear-gradient(rgba(10, 10, 12, 0.88), rgba(10, 10, 12, 0.88)), var(--bg-image);
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-color: #0a0a0c;

    transition: background-image 0.3s ease;
}

.modal-container {
    width: 1100px;
    max-width: 90%;
    display: flex;
    flex-direction: column;
    align-items: center;
}

.modal-header {
    text-align: center;
    width: 100%;
    margin-bottom: 40px;
}

.modal-header h2 {
    color: #c8aa6e;
    font-size: 46px;
    margin: 0;
    text-transform: uppercase;
    letter-spacing: 4px;
    text-shadow: 0 4px 15px rgba(0,0,0,0.9);
}

.modal-body {
    display: flex;
    gap: 60px;
    align-items: center;
    width: 100%;
}

.modal-left {
    flex: 1;
    font-size: 17px;
    line-height: 1.8;
    text-align: justify;
    color: #f0e6d2;
    text-shadow: 0 2px 8px rgba(0,0,0,0.9);
}

.modal-right img {
    width: 500px;
    border-radius: 12px;
    border: 2px solid #c8aa6e;
}

.close-btn {
    position: absolute;
    top: 30px;
    right: 50px;
    font-size: 45px;
    color: #c8aa6e;
    cursor: pointer;
    transition: transform 0.2s, color 0.2s;
    text-shadow: 0 2px 5px rgba(0,0,0,0.5);
}

.close-btn:hover {
    color: #fff;
    transform: scale(1.1);
}

@media (max-width: 950px) {
    .modal-body {
        flex-direction: column-reverse;
        gap: 25px;
    }
    .modal-right img {
        width: 100%;
        max-width: 380px;
    }
    .modal-header h2 {
        font-size: 32px;
    }
    .modal-left {
        font-size: 15px;
    }
}



@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@500;700&display=swap');

body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;

    background: radial-gradient(
        circle at top,
        #1d3557,
        #091428 50%,
        #010a13 100%
    );

    color: #f0e6d2;

    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
    justify-items: center;

    gap: 25px;
    padding: 30px;
}

.champion-card {
    background: linear-gradient(
        180deg,
        #123456,
        #091428 70%,
        #07111f
    );

    border: 2px solid #c8aa6e;
    border-radius: 10px;

    box-shadow:
        0 0 8px rgba(200,170,110,.2),
        0 10px 25px rgba(0,0,0,.6);

    width: 350px;
    padding: 20px;

    display: flex;
    flex-direction: column;
    align-items: center;

    backdrop-filter: blur(6px);

    transition:
        transform .3s ease,
        box-shadow .3s ease;

    animation: apparition .6s ease;
}

.champion-card:hover {
    transform: translateY(-8px);

    box-shadow:
        0 0 20px rgba(200,170,110,.6),
        0 18px 35px rgba(0,0,0,.8);
}

.champion-card h2 {
    font-family: 'Cinzel', serif;
    color: #c8aa6e;
    margin-top: 0;
    text-transform: uppercase;
    letter-spacing: 2px;

    text-shadow:
        0 0 6px rgba(200,170,110,.5);
}

.champion-card h2::after {
    content: "";
    display: block;
    width: 70px;
    height: 3px;
    margin: 10px auto 0;
    background: #c8aa6e;
}

.champion-card img {
    width: 100%;
    border-radius: 5px;
    border: 1px solid #c8aa6e;

    transition: transform .4s;
}

.champion-card:hover img {
    transform: scale(1.04);
}

.description {
    color: #d4c9ae;
    font-size: 15px;
    line-height: 1.8;
    text-align: justify;
    margin-top: 20px;
}

@keyframes apparition {
    from {
        opacity: 0;
        transform: translateY(20px);
    }

    to {
        opacity: 1;
        transform: translateY(0);
    }
}

::-webkit-scrollbar {
    width: 10px;
}

::-webkit-scrollbar-track {
    background: #091428;
}

::-webkit-scrollbar-thumb {
    background: #c8aa6e;
    border-radius: 20px;
}
"""