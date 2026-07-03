css = """
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