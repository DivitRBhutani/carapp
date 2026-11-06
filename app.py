import streamlit as st
from urllib.parse import quote

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="DV Motors | Premium Automotive",
    page_icon="🚘",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =========================================================
# BUSINESS DETAILS
# =========================================================

BUSINESS_NAME = "DV MOTORS"
TAGLINE = "Drive Your Next."
LOCATION = "Queensland, Australia"
PHONE = "+91 8469077711"
WHATSAPP = "918469077711"
EMAIL = "divitbhutani@gmail.com"
HOURS = "8:00 AM – 5:00 PM"


# =========================================================
# VEHICLES
# =========================================================

CARS = [
    {
        "id": 1,
        "brand": "BMW",
        "model": "M4 Competition",
        "year": 2023,
        "price": 139990,
        "fuel": "Petrol",
        "transmission": "Automatic",
        "km": 12500,
        "body": "Coupe",
        "status": "FEATURED",
        "description": "A high-performance BMW combining everyday comfort with serious M performance.",
        "image": "https://images.unsplash.com/photo-1555215695-3004980ad54e?auto=format&fit=crop&w=1600&q=90"
    },
    {
        "id": 2,
        "brand": "Lamborghini",
        "model": "Huracán EVO",
        "year": 2022,
        "price": 349990,
        "fuel": "Petrol",
        "transmission": "Automatic",
        "km": 8200,
        "body": "Coupe",
        "status": "NEW ARRIVAL",
        "description": "Italian performance, dramatic styling and an unforgettable V10 driving experience.",
        "image": "https://images.unsplash.com/photo-1544829099-b9a0c07fad1a?auto=format&fit=crop&w=1600&q=90"
    },
    {
        "id": 3,
        "brand": "Ferrari",
        "model": "SF90 Stradale",
        "year": 2023,
        "price": 549990,
        "fuel": "Hybrid",
        "transmission": "Automatic",
        "km": 6400,
        "body": "Coupe",
        "status": "JUST ARRIVED",
        "description": "A breathtaking Ferrari combining hybrid technology with extraordinary performance.",
        "image": "https://images.unsplash.com/photo-1592198084033-aade902d1aae?auto=format&fit=crop&w=1600&q=90"
    },
    {
        "id": 4,
        "brand": "BMW",
        "model": "M8 Competition",
        "year": 2024,
        "price": 239990,
        "fuel": "Petrol",
        "transmission": "Automatic",
        "km": 5900,
        "body": "Coupe",
        "status": "FEATURED",
        "description": "A refined grand tourer delivering exceptional performance, luxury and comfort.",
        "image": "https://images.unsplash.com/photo-1556189250-72ba954cfc2b?auto=format&fit=crop&w=1600&q=90"
    },
    {
        "id": 5,
        "brand": "Lamborghini",
        "model": "Urus",
        "year": 2023,
        "price": 389990,
        "fuel": "Petrol",
        "transmission": "Automatic",
        "km": 7100,
        "body": "SUV",
        "status": "PREMIUM",
        "description": "Super-SUV performance combined with luxury, practicality and unmistakable styling.",
        "image": "https://images.unsplash.com/photo-1606664515524-ed2f786a0bd6?auto=format&fit=crop&w=1600&q=90"
    },
    {
        "id": 6,
        "brand": "Ferrari",
        "model": "Roma",
        "year": 2022,
        "price": 399990,
        "fuel": "Petrol",
        "transmission": "Automatic",
        "km": 9100,
        "body": "Coupe",
        "status": "AVAILABLE",
        "description": "Elegant Italian grand touring with timeless Ferrari design and thrilling performance.",
        "image": "https://images.unsplash.com/photo-1592853625601-bb9d23da12b0?auto=format&fit=crop&w=1600&q=90"
    }
]


# =========================================================
# SESSION STATE
# =========================================================

if "page" not in st.session_state:
    st.session_state.page = "Home"

if "selected_car" not in st.session_state:
    st.session_state.selected_car = None


# =========================================================
# CSS
# =========================================================

st.html("""
<style>

@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700;800&family=Playfair+Display:wght@600;700&display=swap');

:root {
    --gold: #e5bd68;
    --gold-light: #f2d38a;
    --dark: #07090c;
    --dark2: #0d1014;
    --card: #11151a;
    --border: rgba(255,255,255,0.09);
    --muted: #969ba2;
}

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
}

.stApp {
    background:
        radial-gradient(
            circle at 85% 5%,
            rgba(229,189,104,0.08),
            transparent 27%
        ),
        #07090c;
    color: white;
}

.block-container {
    max-width: 1450px;
    padding-top: 1rem;
    padding-bottom: 3rem;
}

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

.brand-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 12px 5px 18px;
    border-bottom: 1px solid var(--border);
    margin-bottom: 14px;
}

.brand-left {
    display: flex;
    align-items: center;
    gap: 13px;
}

.logo-mark {
    width: 52px;
    height: 31px;
    border-top: 3px solid var(--gold);
    border-radius: 50%;
    display: flex;
    justify-content: center;
    align-items: center;
    color: white;
    font-size: 17px;
    font-weight: 800;
}

.brand-name {
    font-size: 24px;
    font-weight: 800;
    letter-spacing: 4px;
}

.brand-sub {
    color: var(--gold);
    font-size: 8px;
    letter-spacing: 4px;
    margin-top: 4px;
}

.top-contact {
    color: #aeb2b7;
    font-size: 13px;
}

div.stButton > button {
    width: 100%;
    border-radius: 7px;
    min-height: 42px;
    border: 1px solid rgba(255,255,255,0.14);
    background: #11151a;
    color: #eeeeee;
    font-weight: 600;
}

div.stButton > button:hover {
    border-color: var(--gold);
    color: var(--gold);
    background: #151a20;
}

.stLinkButton a {
    border-radius: 7px !important;
    min-height: 42px !important;
    background: var(--gold) !important;
    color: #08090c !important;
    border: none !important;
    font-weight: 700 !important;
}

.hero {
    min-height: 580px;
    border-radius: 22px;
    overflow: hidden;
    display: flex;
    align-items: center;
    background:
        linear-gradient(
            90deg,
            rgba(5,7,9,0.97) 0%,
            rgba(5,7,9,0.90) 30%,
            rgba(5,7,9,0.48) 58%,
            rgba(5,7,9,0.20) 100%
        ),
        url("https://images.unsplash.com/photo-1504215680853-026ed2a45def?auto=format&fit=crop&w=2200&q=90");
    background-size: cover;
    background-position: center;
}

.hero-content {
    padding: 65px;
    max-width: 720px;
}

.hero-kicker {
    color: var(--gold);
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 4px;
    margin-bottom: 18px;
}

.hero-title {
    font-family: 'Playfair Display', serif;
    font-size: clamp(50px, 7vw, 86px);
    line-height: 0.95;
    margin: 0;
}

.gold {
    color: var(--gold);
}

.hero-tagline {
    font-size: 26px;
    margin-top: 16px;
}

.hero-description {
    color: #c4c7ca;
    font-size: 16px;
    line-height: 1.8;
    max-width: 570px;
    margin-top: 20px;
}

.section {
    margin-top: 65px;
}

.kicker {
    color: var(--gold);
    font-size: 10px;
    font-weight: 700;
    letter-spacing: 3px;
    text-transform: uppercase;
}

.section-title {
    font-family: 'Playfair Display', serif;
    font-size: 40px;
    margin-top: 5px;
}

.section-description {
    color: var(--muted);
    max-width: 600px;
    line-height: 1.6;
}

.search-box {
    background: rgba(15,18,23,0.96);
    border: 1px solid rgba(255,255,255,0.12);
    border-radius: 14px;
    padding: 18px;
    margin-top: 22px;
}

.stat {
    background: linear-gradient(145deg, #12161b, #0d1014);
    border: 1px solid var(--border);
    border-radius: 13px;
    padding: 25px;
    text-align: center;
}

.stat-number {
    color: var(--gold);
    font-size: 29px;
    font-weight: 800;
}

.stat-label {
    color: #888e95;
    font-size: 12px;
    margin-top: 5px;
}

.car-card {
    background: #101318;
    border: 1px solid var(--border);
    border-radius: 15px;
    overflow: hidden;
    margin-bottom: 10px;
}

.car-card img {
    width: 100%;
    height: 225px;
    object-fit: cover;
    display: block;
}

.car-info {
    padding: 19px;
}

.badge {
    display: inline-block;
    color: var(--gold);
    background: rgba(229,189,104,0.12);
    padding: 5px 9px;
    border-radius: 5px;
    font-size: 9px;
    font-weight: 800;
    letter-spacing: 1px;
}

.car-brand {
    color: #858b92;
    font-size: 12px;
    margin-top: 13px;
}

.car-model {
    font-size: 22px;
    font-weight: 700;
    margin-top: 3px;
}

.car-spec {
    color: #92979e;
    font-size: 11px;
    margin-top: 10px;
}

.car-price {
    color: var(--gold);
    font-size: 21px;
    font-weight: 800;
    margin-top: 12px;
}

.feature {
    background: linear-gradient(145deg, #14181d, #0c0f13);
    border: 1px solid var(--border);
    border-radius: 14px;
    padding: 28px;
    min-height: 175px;
}

.feature-icon {
    color: var(--gold);
    font-size: 25px;
}

.feature-title {
    font-size: 18px;
    font-weight: 700;
    margin-top: 17px;
}

.feature-text {
    color: #8e949b;
    font-size: 13px;
    line-height: 1.7;
    margin-top: 7px;
}

.about {
    background: linear-gradient(135deg, #15191f, #0d1014);
    border: 1px solid var(--border);
    border-radius: 18px;
    padding: 45px;
}

.about-title {
    font-family: 'Playfair Display', serif;
    font-size: 40px;
}

.about-text {
    color: #aeb3b8;
    line-height: 1.8;
    font-size: 15px;
}

.contact-box {
    background: #11151a;
    border: 1px solid var(--border);
    border-radius: 13px;
    padding: 22px;
    margin-bottom: 13px;
}

.contact-label {
    color: #777e86;
    font-size: 9px;
    letter-spacing: 2px;
    text-transform: uppercase;
}

.contact-value {
    font-size: 16px;
    margin-top: 7px;
}

.footer {
    margin-top: 80px;
    padding: 38px 0 10px;
    border-top: 1px solid var(--border);
    text-align: center;
    color: #737980;
    font-size: 12px;
}

.footer-brand {
    color: white;
    font-size: 21px;
    letter-spacing: 5px;
    font-weight: 800;
}

</style>
""")


# =========================================================
# FUNCTIONS
# =========================================================

def money(price):
    return f"AUD ${price:,.0f}"


def navigate(page):
    st.session_state.page = page
    st.rerun()


def whatsapp_url(car_name=""):
    if car_name:
        message = f"Hi DV Motors, I am interested in the {car_name}."
    else:
        message = "Hi DV Motors, I would like to make an enquiry."

    return "https://wa.me/" + WHATSAPP + "?text=" + quote(message)


def show_car_card(car, key_prefix):

    st.html(
        f"""
        <div class="car-card">

            <img src="{car['image']}">

            <div class="car-info">

                <span class="badge">
                    {car['status']}
                </span>

                <div class="car-brand">
                    {car['brand']}
                </div>

                <div class="car-model">
                    {car['model']}
                </div>

                <div class="car-spec">
                    {car['year']} &nbsp; • &nbsp;
                    {car['fuel']} &nbsp; • &nbsp;
                    {car['transmission']} &nbsp; • &nbsp;
                    {car['km']:,} km
                </div>

                <div class="car-price">
                    {money(car['price'])}
                </div>

            </div>

        </div>
        """
    )

    a, b = st.columns(2)

    with a:
        if st.button(
            "View Details",
            key=f"{key_prefix}_details",
            use_container_width=True
        ):
            st.session_state.selected_car = car
            navigate("Car Details")

    with b:
        st.link_button(
            "WhatsApp",
            whatsapp_url(
                car["brand"] + " " + car["model"]
            ),
            use_container_width=True
        )


def footer():

    st.html(
        f"""
        <div class="footer">

            <div class="footer-brand">
                DV MOTORS
            </div>

            <div style="margin-top:8px;">
                Drive Your Next.
            </div>

            <div style="margin-top:15px;">
                {LOCATION}
                &nbsp; • &nbsp;
                {PHONE}
                &nbsp; • &nbsp;
                {EMAIL}
            </div>

            <div style="margin-top:15px;">
                Open {HOURS}
            </div>

            <div style="margin-top:22px;">
                © 2026 DV Motors. All rights reserved.
            </div>

        </div>
        """
    )


# =========================================================
# HEADER
# =========================================================

st.html(
    """
    <div class="brand-header">

        <div class="brand-left">

            <div class="logo-mark">
                DV
            </div>

            <div>

                <div class="brand-name">
                    DV MOTORS
                </div>

                <div class="brand-sub">
                    PREMIUM AUTOMOTIVE
                </div>

            </div>

        </div>

        <div class="top-contact">
            Queensland, Australia &nbsp; • &nbsp;
            +91 8469077711
        </div>

    </div>
    """
)


# =========================================================
# NAVIGATION
# =========================================================

nav = st.columns(6)

navigation = [
    "Home",
    "Inventory",
    "Featured Cars",
    "Sell / Exchange",
    "About Us",
    "Contact"
]

for i, item in enumerate(navigation):

    with nav[i]:

        if st.button(
            item,
            key="nav_" + item,
            use_container_width=True
        ):
            navigate(item)


# =========================================================
# HOME PAGE
# =========================================================

if st.session_state.page == "Home":

    st.html(
        """
        <div class="hero">

            <div class="hero-content">

                <div class="hero-kicker">
                    PREMIUM CARS · QUEENSLAND
                </div>

                <div class="hero-title">
                    DV <span class="gold">MOTORS</span>
                </div>

                <div class="hero-tagline">
                    Drive Your Next.
                </div>

                <div class="hero-description">
                    Discover a carefully selected collection
                    of performance, luxury and prestige vehicles.
                    Your next dream car starts here.
                </div>

            </div>

        </div>
        """
    )

    st.html(
        """
        <div class="search-box">

            <div class="kicker">
                FIND YOUR NEXT CAR
            </div>

        </div>
        """
    )

    s1, s2, s3, s4 = st.columns(4)

    with s1:
        home_brand = st.selectbox(
            "Brand",
            ["All Brands"] + sorted(
                set(car["brand"] for car in CARS)
            ),
            key="home_brand"
        )

    with s2:
        home_fuel = st.selectbox(
            "Fuel Type",
            ["All Fuel Types", "Petrol", "Hybrid"],
            key="home_fuel"
        )

    with s3:
        home_transmission = st.selectbox(
            "Transmission",
            ["All Transmissions", "Automatic", "Manual"],
            key="home_transmission"
        )

    with s4:

        st.write("")
        st.write("")

        if st.button(
            "SEARCH INVENTORY  →",
            key="home_search",
            use_container_width=True
        ):

            st.session_state.inventory_brand = home_brand
            st.session_state.inventory_fuel = home_fuel
            st.session_state.inventory_transmission = home_transmission

            navigate("Inventory")

    st.markdown("<br>", unsafe_allow_html=True)

    stat_columns = st.columns(4)

    statistics = [
        ("25+", "Vehicles Available"),
        ("10+", "Premium Brands"),
        ("100%", "Customer Focused"),
        ("8 AM – 5 PM", "Opening Hours")
    ]

    for col, item in zip(stat_columns, statistics):

        number, label = item

        with col:

            st.html(
                f"""
                <div class="stat">

                    <div class="stat-number">
                        {number}
                    </div>

                    <div class="stat-label">
                        {label}
                    </div>

                </div>
                """
            )

    st.html(
        """
        <div class="section">

            <div class="kicker">
                OUR COLLECTION
            </div>

            <div class="section-title">
                Featured <span class="gold">Cars</span>
            </div>

            <div class="section-description">
                A selection of premium vehicles from our
                example collection.
            </div>

        </div>
        """
    )

    columns = st.columns(3)

    for col, car in zip(columns, CARS[:3]):

        with col:
            show_car_card(
                car,
                "home_" + str(car["id"])
            )

    st.html(
        """
        <div class="section">

            <div class="kicker">
                THE DV DIFFERENCE
            </div>

            <div class="section-title">
                Why Choose <span class="gold">DV Motors?</span>
            </div>

        </div>
        """
    )

    features = [
        (
            "01",
            "Premium Selection",
            "A carefully selected range of performance, luxury and prestige vehicles."
        ),
        (
            "02",
            "Quality Focused",
            "We focus on presentation, vehicle condition and customer confidence."
        ),
        (
            "03",
            "Transparent Service",
            "Straightforward communication and clear vehicle information."
        ),
        (
            "04",
            "Personal Assistance",
            "Support from discovering a vehicle through to your enquiry."
        )
    ]

    columns = st.columns(4)

    for col, feature in zip(columns, features):

        number, title, description = feature

        with col:

            st.html(
                f"""
                <div class="feature">

                    <div class="feature-icon">
                        {number}
                    </div>

                    <div class="feature-title">
                        {title}
                    </div>

                    <div class="feature-text">
                        {description}
                    </div>

                </div>
                """
            )


# =========================================================
# INVENTORY
# =========================================================

elif st.session_state.page == "Inventory":

    st.html(
        """
        <div class="section">

            <div class="kicker">
                EXPLORE OUR CARS
            </div>

            <div class="section-title">
                Vehicle <span class="gold">Inventory</span>
            </div>

            <div class="section-description">
                Browse our example collection of premium,
                performance and luxury vehicles.
            </div>

        </div>
        """
    )

    brand_options = [
        "All Brands"
    ] + sorted(
        set(car["brand"] for car in CARS)
    )

    fuel_options = [
        "All Fuel Types",
        "Petrol",
        "Hybrid"
    ]

    transmission_options = [
        "All Transmissions",
        "Automatic",
        "Manual"
    ]

    default_brand = st.session_state.get(
        "inventory_brand",
        "All Brands"
    )

    default_fuel = st.session_state.get(
        "inventory_fuel",
        "All Fuel Types"
    )

    default_transmission = st.session_state.get(
        "inventory_transmission",
        "All Transmissions"
    )

    f1, f2, f3, f4 = st.columns(4)

    with f1:

        brand = st.selectbox(
            "Brand",
            brand_options,
            index=(
                brand_options.index(default_brand)
                if default_brand in brand_options
                else 0
            )
        )

    with f2:

        fuel = st.selectbox(
            "Fuel",
            fuel_options,
            index=(
                fuel_options.index(default_fuel)
                if default_fuel in fuel_options
                else 0
            )
        )

    with f3:

        transmission = st.selectbox(
            "Transmission",
            transmission_options,
            index=(
                transmission_options.index(default_transmission)
                if default_transmission in transmission_options
                else 0
            )
        )

    with f4:

        price_limit = st.selectbox(
            "Maximum Price",
            [
                "Any Price",
                "AUD $150,000",
                "AUD $250,000",
                "AUD $400,000",
                "AUD $600,000"
            ]
        )

    filtered = CARS.copy()

    if brand != "All Brands":

        filtered = [
            car for car in filtered
            if car["brand"] == brand
        ]

    if fuel != "All Fuel Types":

        filtered = [
            car for car in filtered
            if car["fuel"] == fuel
        ]

    if transmission != "All Transmissions":

        filtered = [
            car for car in filtered
            if car["transmission"] == transmission
        ]

    if price_limit != "Any Price":

        limit = int(
            price_limit
            .replace("AUD $", "")
            .replace(",", "")
        )

        filtered = [
            car for car in filtered
            if car["price"] <= limit
        ]

    st.html(
        f"""
        <div style="
            color:#858b92;
            margin:25px 0 18px;
            font-size:13px;
        ">
            Showing
            <span style="
                color:#e5bd68;
                font-weight:700;
            ">
                {len(filtered)}
            </span>
            vehicles
        </div>
        """
    )

    if not filtered:

        st.warning(
            "No vehicles match your selected filters."
        )

    else:

        for start in range(
            0,
            len(filtered),
            3
        ):

            row = st.columns(3)

            for position in range(3):

                if start + position < len(filtered):

                    car = filtered[
                        start + position
                    ]

                    with row[position]:

                        show_car_card(
                            car,
                            "inventory_" + str(car["id"])
                        )


# =========================================================
# CAR DETAILS
# =========================================================

elif st.session_state.page == "Car Details":

    car = st.session_state.selected_car

    if car is None:

        navigate("Inventory")

    if st.button("← BACK TO INVENTORY"):

        navigate("Inventory")

    st.markdown("<br>", unsafe_allow_html=True)

    image_col, detail_col = st.columns(
        [1.25, 1]
    )

    with image_col:

        st.image(
            car["image"],
            use_container_width=True
        )

    with detail_col:

        st.html(
            f"""
            <span class="badge">
                {car['status']}
            </span>

            <div class="car-brand">
                {car['brand']}
            </div>

            <div style="
                font-size:44px;
                font-weight:800;
                margin-top:4px;
            ">
                {car['model']}
            </div>

            <div class="car-price"
                 style="font-size:30px;">
                {money(car['price'])}
            </div>

            <div style="
                color:#92979e;
                line-height:1.8;
                margin-top:20px;
            ">
                {car['description']}
            </div>
            """
        )

        st.markdown("---")

        d1, d2 = st.columns(2)

        with d1:

            st.write("**Year**")
            st.write(car["year"])

            st.write("**Fuel**")
            st.write(car["fuel"])

            st.write("**Body**")
            st.write(car["body"])

        with d2:

            st.write("**Transmission**")
            st.write(car["transmission"])

            st.write("**Kilometres**")
            st.write(f"{car['km']:,} km")

        st.markdown("<br>", unsafe_allow_html=True)

        st.link_button(
            "💬 ENQUIRE ON WHATSAPP",
            whatsapp_url(
                car["brand"] + " " + car["model"]
            ),
            use_container_width=True
        )

        if st.button(
            "📞 REQUEST A CALLBACK",
            use_container_width=True
        ):

            navigate("Contact")


# =========================================================
# FEATURED CARS
# =========================================================

elif st.session_state.page == "Featured Cars":

    st.html(
        """
        <div class="section">

            <div class="kicker">
                HAND-PICKED
            </div>

            <div class="section-title">
                Featured <span class="gold">Collection</span>
            </div>

            <div class="section-description">
                Discover some of the standout vehicles
                in our example collection.
            </div>

        </div>
        """
    )

    for car in CARS[:4]:

        left, right = st.columns(
            [1.15, 1]
        )

        with left:

            st.image(
                car["image"],
                use_container_width=True
            )

        with right:

            st.html(
                f"""
                <span class="badge">
                    {car['status']}
                </span>

                <div class="car-brand">
                    {car['brand']}
                </div>

                <div style="
                    font-size:32px;
                    font-weight:800;
                    margin-top:4px;
                ">
                    {car['model']}
                </div>

                <div class="car-price">
                    {money(car['price'])}
                </div>

                <div style="
                    color:#969ba2;
                    line-height:1.7;
                    margin-top:14px;
                ">
                    {car['description']}
                </div>

                <div style="
                    color:#888e95;
                    font-size:12px;
                    margin-top:15px;
                ">
                    {car['year']} &nbsp; • &nbsp;
                    {car['fuel']} &nbsp; • &nbsp;
                    {car['transmission']} &nbsp; • &nbsp;
                    {car['km']:,} km
                </div>
                """
            )

            st.markdown("<br>", unsafe_allow_html=True)

            a, b = st.columns(2)

            with a:

                if st.button(
                    "View Vehicle",
                    key="featured_view_" + str(car["id"]),
                    use_container_width=True
                ):

                    st.session_state.selected_car = car
                    navigate("Car Details")

            with b:

                st.link_button(
                    "WhatsApp",
                    whatsapp_url(
                        car["brand"] + " " + car["model"]
                    ),
                    use_container_width=True
                )

        st.markdown("---")


# =========================================================
# SELL / EXCHANGE
# =========================================================

elif st.session_state.page == "Sell / Exchange":

    st.html(
        """
        <div class="section">

            <div class="kicker">
                UPGRADE YOUR DRIVE
            </div>

            <div class="section-title">
                Sell or <span class="gold">Exchange</span>
            </div>

            <div class="section-description">
                Thinking about upgrading?
                Tell us about your current vehicle.
            </div>

        </div>
        """
    )

    left, right = st.columns(
        [1.15, 0.85]
    )

    with left:

        with st.form("exchange_form"):

            name = st.text_input(
                "Full Name *"
            )

            phone = st.text_input(
                "Phone Number *"
            )

            email = st.text_input(
                "Email Address"
            )

            current_car = st.text_input(
                "Current Car *"
            )

            year = st.number_input(
                "Vehicle Year",
                min_value=1990,
                max_value=2026,
                value=2020
            )

            kilometres = st.number_input(
                "Kilometres Driven",
                min_value=0,
                value=50000
            )

            request = st.radio(
                "What would you like to do?",
                [
                    "Sell My Car",
                    "Exchange My Car"
                ]
            )

            message = st.text_area(
                "Additional Information"
            )

            submit = st.form_submit_button(
                "SUBMIT ENQUIRY",
                use_container_width=True
            )

            if submit:

                if name and phone and current_car:

                    st.success(
                        "Thank you! Your enquiry has been received."
                    )

                else:

                    st.error(
                        "Please complete all required fields."
                    )

    with right:

        st.html(
            """
            <div class="about">

                <div class="kicker">
                    DV MOTORS
                </div>

                <div class="about-title">
                    Your next car
                    <span class="gold">
                        could be closer
                    </span>
                    than you think.
                </div>

                <br>

                <div class="about-text">
                    Whether you want to sell your current
                    vehicle or exchange it for something new,
                    start the conversation with DV Motors.
                </div>

                <br>

                <div class="about-text">
                    ✓ Simple enquiry process<br><br>
                    ✓ Personal assistance<br><br>
                    ✓ Premium vehicle selection<br><br>
                    ✓ Straightforward communication
                </div>

            </div>
            """
        )


# =========================================================
# ABOUT US
# =========================================================

elif st.session_state.page == "About Us":

    st.html(
        """
        <div class="section">

            <div class="kicker">
                WHO WE ARE
            </div>

            <div class="section-title">
                About <span class="gold">DV Motors</span>
            </div>

        </div>

        <div class="about">

            <div class="about-title">
                More than a showroom.
                <br>
                <span class="gold">
                    A better way to buy.
                </span>
            </div>

            <br>

            <div class="about-text">

                DV Motors is a premium automotive dealership
                concept based in Queensland, Australia,
                focused on performance, luxury and prestige
                vehicles.

                <br><br>

                We believe buying a car should feel exciting,
                straightforward and personal.

                <br><br>

                From discovering the right vehicle to making
                an enquiry, our goal is to create a smooth
                experience built around quality, transparency
                and customer confidence.

            </div>

        </div>
        """
    )

    st.html(
        """
        <div class="section">

            <div class="kicker">
                OUR VALUES
            </div>

            <div class="section-title">
                What We <span class="gold">Stand For</span>
            </div>

        </div>
        """
    )

    values = [
        (
            "01",
            "QUALITY",
            "We focus on presenting vehicles with strong attention to quality and presentation."
        ),
        (
            "02",
            "TRUST",
            "Clear information and straightforward communication are central to our approach."
        ),
        (
            "03",
            "PASSION",
            "Cars should be more than transportation. They should be something you enjoy."
        )
    ]

    cols = st.columns(3)

    for col, value in zip(cols, values):

        number, title, description = value

        with col:

            st.html(
                f"""
                <div class="feature">

                    <div class="feature-icon">
                        {number}
                    </div>

                    <div class="feature-title">
                        {title}
                    </div>

                    <div class="feature-text">
                        {description}
                    </div>

                </div>
                """
            )


# =========================================================
# CONTACT
# =========================================================

elif st.session_state.page == "Contact":

    st.html(
        """
        <div class="section">

            <div class="kicker">
                LET'S TALK
            </div>

            <div class="section-title">
                Contact <span class="gold">DV Motors</span>
            </div>

            <div class="section-description">
                Have a question about a vehicle or want to
                make an enquiry? Get in touch.
            </div>

        </div>
        """
    )

    left, right = st.columns(
        [0.9, 1.1]
    )

    with left:

        st.html(
            f"""
            <div class="contact-box">

                <div class="contact-label">
                    LOCATION
                </div>

                <div class="contact-value">
                    📍 {LOCATION}
                </div>

            </div>

            <div class="contact-box">

                <div class="contact-label">
                    PHONE
                </div>

                <div class="contact-value">
                    📞 {PHONE}
                </div>

            </div>

            <div class="contact-box">

                <div class="contact-label">
                    WHATSAPP
                </div>

                <div class="contact-value">
                    💬 {PHONE}
                </div>

            </div>

            <div class="contact-box">

                <div class="contact-label">
                    EMAIL
                </div>

                <div class="contact-value">
                    ✉️ {EMAIL}
                </div>

            </div>

            <div class="contact-box">

                <div class="contact-label">
                    OPENING HOURS
                </div>

                <div class="contact-value">
                    🕐 {HOURS}
                </div>

            </div>
            """
        )

        st.link_button(
            "💬 CHAT ON WHATSAPP",
            "https://wa.me/" + WHATSAPP,
            use_container_width=True
        )

    with right:

        st.html(
            """
            <div class="about">

                <div class="kicker">
                    SEND AN ENQUIRY
                </div>

                <div class="about-title">
                    Let's find your
                    <span class="gold">
                        next car.
                    </span>
                </div>

            </div>
            """
        )

        name = st.text_input(
            "Name",
            key="contact_name"
        )

        contact_phone = st.text_input(
            "Phone",
            key="contact_phone"
        )

        contact_email = st.text_input(
            "Email",
            key="contact_email"
        )

        enquiry_type = st.selectbox(
            "I'm interested in",
            [
                "Buying a vehicle",
                "Selling my vehicle",
                "Exchanging my vehicle",
                "General enquiry"
            ]
        )

        message = st.text_area(
            "Message",
            key="contact_message"
        )

        if st.button(
            "SEND ENQUIRY",
            key="send_contact",
            use_container_width=True
        ):

            if name and contact_phone and message:

                st.success(
                    "Thanks! Your enquiry has been received."
                )

            else:

                st.warning(
                    "Please enter your name, phone number and message."
                )


# =========================================================
# FOOTER
# =========================================================

footer()