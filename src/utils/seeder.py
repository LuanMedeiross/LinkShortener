import requests

# Lista de 200+ URLs famosas de diversos escopos
urls = [
    # Tecnologia
    "https://www.google.com", "https://www.apple.com", "https://www.microsoft.com", "https://www.amazon.com",
    "https://www.facebook.com", "https://www.instagram.com", "https://www.whatsapp.com", "https://www.youtube.com",
    "https://www.tiktok.com", "https://www.netflix.com", "https://www.spotify.com", "https://www.twitch.tv",
    "https://www.github.com", "https://www.stackoverflow.com", "https://www.reddit.com", "https://www.linkedin.com",
    "https://www.dropbox.com", "https://www.salesforce.com", "https://www.adobe.com", "https://www.nvidia.com",

    # Educação
    "https://www.khanacademy.org", "https://www.coursera.org", "https://www.udemy.com", "https://www.edx.org",
    "https://www.udacity.com", "https://www.codecademy.com", "https://www.duolingo.com", "https://www.academia.edu",
    "https://www.researchgate.net", "https://www.sciencedirect.com",

    # Bancos e Finanças
    "https://www.paypal.com", "https://www.nubank.com.br", "https://www.itau.com.br", "https://www.bb.com.br",
    "https://www.santander.com.br", "https://www.c6bank.com.br", "https://www.bradesco.com.br",
    "https://www.binance.com", "https://www.coinbase.com", "https://www.blockchain.com",

    # Notícias
    "https://www.cnn.com", "https://www.bbc.com", "https://www.nytimes.com", "https://www.theguardian.com",
    "https://www.reuters.com", "https://www.uol.com.br", "https://www.g1.globo.com", "https://www.estadao.com.br",
    "https://www.folha.uol.com.br", "https://www.terra.com.br",

    # Compras e Varejo
    "https://www.mercadolivre.com.br", "https://www.ebay.com", "https://www.walmart.com", "https://www.aliexpress.com",
    "https://www.magazineluiza.com.br", "https://www.americanas.com.br", "https://www.kabum.com.br",
    "https://www.shopee.com.br", "https://www.submarino.com.br", "https://www.zalando.com",

    # Viagem e Transporte
    "https://www.booking.com", "https://www.airbnb.com", "https://www.uber.com", "https://www.lyft.com",
    "https://www.trivago.com", "https://www.kayak.com", "https://www.decolar.com", "https://www.avianca.com",
    "https://www.latam.com", "https://www.voegol.com.br",

    # Jogos
    "https://store.steampowered.com", "https://www.epicgames.com", "https://www.roblox.com", "https://www.minecraft.net",
    "https://www.riotgames.com", "https://www.battle.net", "https://www.playstation.com", "https://www.xbox.com",

    # Governo/Oficiais
    "https://www.gov.br", "https://www.receita.fazenda.gov.br", "https://www.inss.gov.br", "https://www.bcb.gov.br",
    "https://www.planalto.gov.br", "https://www.tse.jus.br", "https://www.stf.jus.br", "https://www.camara.leg.br",

    # Saúde
    "https://www.who.int", "https://www.ms.gov.br", "https://www.hopkinsmedicine.org", "https://www.mayoclinic.org",
    "https://www.doctoralia.com.br", "https://www.healthychildren.org",

    # Diversos
    "https://www.imdb.com", "https://www.weather.com", "https://www.speedtest.net", "https://www.canva.com",
    "https://www.medium.com", "https://www.pinterest.com", "https://www.figma.com", "https://www.trello.com",
    "https://www.notion.so", "https://www.slack.com", "https://www.zoom.us", "https://www.mozilla.org",
    "https://www.vivaldi.com", "https://www.opera.com", "https://www.yandex.com", "https://www.duckduckgo.com",
    "https://www.archive.org", "https://www.pexels.com", "https://www.unsplash.com", "https://www.freepik.com",
    "https://www.pixabay.com", "https://www.deviantart.com", "https://www.behance.net", "https://www.dribbble.com",
    "https://www.soundcloud.com", "https://www.bandcamp.com", "https://www.shazam.com", "https://www.tunein.com",
    "https://www.goodreads.com", "https://www.wikipedia.org", "https://www.wikihow.com", "https://www.quora.com",
    "https://www.stackexchange.com", "https://www.npmjs.com", "https://www.pypi.org", "https://www.jetbrains.com",
    "https://www.visualstudio.com", "https://www.eclipse.org", "https://www.qt.io", "https://www.gnu.org",
    "https://www.linux.org", "https://www.kernel.org", "https://www.debian.org", "https://www.archlinux.org",
    "https://www.kali.org", "https://www.raspberrypi.org", "https://www.virtualbox.org", "https://www.vagrantup.com",
    "https://www.docker.com", "https://www.kubernetes.io", "https://www.heroku.com", "https://www.digitalocean.com",
    "https://www.cloudflare.com", "https://www.vercel.com", "https://www.netlify.com",
]

# Envio dos POSTs com header "url"
for i, url in enumerate(urls, start=1):
    try:
        response = requests.post("http://localhost:8000/shorten", headers={"host": "localhost:8000"}, json={"url": url})
        print(f"[{i:03}] {url} => Status: {response.status_code}")
    except Exception as e:
        print(f"[{i:03}] {url} => ERRO: {e}")
