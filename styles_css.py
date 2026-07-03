css = """
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@500;700&display=swap');

    body {
        margin: 0;
        padding: 30px;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        background: radial-gradient(circle at top, #1d3557, #091428 50%, #010a13 100%);
        color: #f0e6d2;
    }

    main {
        display: grid;
        grid-template-columns: repeat(5, minmax(200px, 1fr));
        justify-items: center;
        gap: 25px;
    }

    header {
        text-align: center;
        margin-bottom: 20px;
        padding: 20px 10px;

        background: linear-gradient(90deg, rgba(10,20,35,0.8), rgba(20,30,50,0.6), rgba(10,20,35,0.8));
        border-bottom: 1px solid #c8aa6e;

        box-shadow: 0 8px 20px rgba(0,0,0,.4);
    }

    header h1 {
        font-family: 'Cinzel', serif;
        color: #c8aa6e;
        letter-spacing: 3px;
        text-transform: uppercase;
        margin-bottom: 8px;
    }

    header p {
        color: #f0e6d2;
        opacity: 0.8;
        font-size: 14px;
    }

    #search {
        width: 70%;
        max-width: 600px;

        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 10px;

        margin: 30px auto;
        padding: 20px;

        background: rgba(10, 20, 35, 0.6);
        border: 1px solid #c8aa6e;
        border-radius: 12px;

        box-shadow: 0 10px 30px rgba(0,0,0,.5);
        backdrop-filter: blur(8px);
    }

    #search label {
        font-family: 'Cinzel', serif;
        color: #c8aa6e;
        letter-spacing: 1px;
        font-size: 14px;
        text-transform: uppercase;
    }

    #searcher {
        width: 280px;
        padding: 10px 14px;

        border-radius: 8px;
        border: 1px solid #c8aa6e;

        background: rgba(255,255,255,0.9);
        color: #091428;

        outline: none;

        transition: 0.2s ease;
    }

    #searcher:focus {
        transform: scale(1.03);
        box-shadow: 0 0 12px rgba(200,170,110,.6);
        border-color: #fff;
    }

    #submitter {
        padding: 10px 18px;
        width: 40%;
        min-width: 50px;
        border-radius: 10px;
        border: 1px solid #c8aa6e;

        background: linear-gradient(135deg, #c8aa6e, #8a6f3b);
        color: #091428;

        font-weight: bold;
        cursor: pointer;

        transition: 0.2s ease;
    }

    #submitter:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 18px rgba(0,0,0,.5);
    }

    #submitter:active {
        transform: translateY(0px);
    }

    /* CARD CHAMPION */
    .champion-item {
        width: 320px;
        display: flex;
        flex-direction: column;
        align-items: center;
        cursor: pointer;

        background: linear-gradient(180deg, #123456, #091428 70%, #07111f);
        border: 2px solid #c8aa6e;
        border-radius: 10px;

        box-shadow: 0 10px 25px rgba(0,0,0,.6);
        padding: 15px;

        transition: transform .3s ease, box-shadow .3s ease;
        animation: apparition .5s ease;
    }

    .champion-item:hover {
        box-shadow: 0 0 25px rgba(200,170,110,.35),
                0 18px 35px rgba(0,0,0,.8);
    }

    .champion-img {
        width: 100%;
        background: opacity(0);
        border-radius: 8px;
        border: 1px solid #c8aa6e;
        transition: transform .35s ease, filter .35s ease;
    }

    .champion-item:hover .champion-img {
        filter: brightness(1.1) contrast(1.05);
    }

    .champion-name {
        font-family: 'Cinzel', serif;
        color: #c8aa6e;
        margin-top: 12px;
        font-size: 16px;
        text-transform: uppercase;
        letter-spacing: 2px;
        text-align: center;
    }

    .role-badge {
        font-family: 'Cinzel', serif;
        text-align: center;
        font-size: 12px;
    }

    /* MODAL */
    .modal {
        display: none;
        position: fixed;
        inset: 0;
        z-index: 9999;

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
        font-size: 1.3em;

        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;

        background: linear-gradient(rgba(10,10,12,0.9), rgba(10,10,12,0.9));
        backdrop-filter: blur(6px);
    }

    .modal-header h2 {
        font-family: 'Cinzel', serif;
        color: #c8aa6e;
        text-transform: uppercase;
        letter-spacing: 4px;
        margin-bottom: 30px;
        text-align: left;
    }

    .modal-body {
        display: flex;
        gap: 50px;
        align-items: center;
        max-width: 1100px;
    }

    .modal-left {
        flex: 1;
        line-height: 1.5;
        text-align: justify;
    }

    .modal-right img {
        width: 450px;
        border-radius: 12px;
        border: 2px solid #c8aa6e;
    }

    /* CLOSE BTN */
    .close-btn {
        position: absolute;
        top: 25px;
        right: 40px;
        font-size: 40px;
        color: #c8aa6e;
        cursor: pointer;
        transition: .2s;
    }

    .close-btn:hover {
        color: #fff;
        transform: scale(1.1);
    }

    /* ANIMATION */
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

    /* RESPONSIVE */
    @media (max-width: 900px) {
        .modal-body {
            flex-direction: column-reverse;
            gap: 20px;
        }

        .modal-right img {
            width: 100%;
            max-width: 380px;
        }

        .modal-header h2 {
            font-size: 28px;
        }
    }
"""