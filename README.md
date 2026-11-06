DV Motors --- Premium Automotive
A Streamlit-based showcase website for DV Motors, a premium
automotive dealership concept. The app presents a vehicle collection,
lets visitors browse and filter inventory, view individual vehicle
details, and start enquiries through WhatsApp or on-page forms.

Tagline: Drive Your Next.
Features
- Home page with a hero section, business highlights, featured
  vehicles, and service/value statements.
- Vehicle inventory with filters for:
  - Brand
  - Fuel type
  - Transmission
  - Maximum price
- Vehicle details including year, fuel, transmission, body type,
  kilometres driven, description, price, and enquiry link.
- Featured Cars page highlighting selected vehicles.
- Sell / Exchange enquiry form for visitors interested in selling
  or exchanging a vehicle.
- About Us page describing the business concept and its values.
- Contact page with business contact details and an enquiry form.
- WhatsApp enquiry links with a pre-filled message for individual
  vehicles.
- Custom dark styling with gold accents, responsive Streamlit columns,
  and vehicle imagery.
Tech Stack
- Python
- Streamlit
- HTML and CSS embedded through Streamlit
- Unsplash-hosted images
- WhatsApp click-to-chat links
Project Structure
The supplied application is written as a single Streamlit Python file.
dv-motors/
├── app.py
└── README.md
Save the supplied application code as app.py. If you use a different
filename, replace app.py in the run command below with that filename.
Requirements
- Python 3.9 or newer is recommended.
- pip
- An internet connection for externally hosted vehicle images and
  Google Fonts.
Install Streamlit:
python -m pip install streamlit
Run Locally
1. Save the application code as app.py.
2. Open a terminal in the project directory.
3. Install the dependency:
   python -m pip install streamlit
4. Start the app:
   streamlit run app.py
5. Streamlit will print a local URL (usually http://localhost:8501).
   Open it in your browser.
Vehicle Collection
The current sample inventory contains six vehicles:

  Vehicle                     Year Fuel     Transmission             Price
  BMW M4 Competition          2023 Petrol   Automatic        AUD $139,990
Lamborghini Huracán EVO     2022 Petrol   Automatic        AUD $349,990
Ferrari SF90 Stradale       2023 Hybrid   Automatic        AUD $549,990
BMW M8 Competition          2024 Petrol   Automatic        AUD $239,990
Lamborghini Urus            2023 Petrol   Automatic        AUD $389,990
Ferrari Roma                2022 Petrol   Automatic        AUD $399,990

Vehicle records are stored in the CARS list near the top of the Python
file. Update that list to change vehicle details, prices, status labels,
descriptions, mileage, or image URLs.
Configuration
Business information is stored near the top of the application in these
constants:
- BUSINESS_NAME
- TAGLINE
- LOCATION
- PHONE
- WHATSAPP
- EMAIL
- HOURS
Update these values before publishing the app. The WhatsApp value should
be the international phone number in digits-only format, including the
country code.

Prices are formatted as Australian dollars (AUD) by the money()
function.
How Enquiries Work
- Vehicle WhatsApp buttons open a chat with a pre-filled
  vehicle-specific message.
- The general WhatsApp button opens a chat with the configured
  business number.
- The Sell / Exchange and Contact forms currently validate required
  fields and display an on-screen confirmation message.
Important: The supplied code does not connect the forms to an email
service, database, CRM, or other storage. Form submissions are not
actually transmitted or saved. Connect a secure backend or
form-processing service before relying on these forms for real customer
enquiries.
Notes Before Deployment
Review the following before making the site public:
1. Business details: Confirm the location, phone number, WhatsApp
   number, email address, and opening hours are correct and consistent.
2. Inventory: The six vehicles in CARS are the records currently
   displayed. Replace sample records with accurate, authorized
   listings.
3. Homepage statistics: The homepage displays promotional figures
   such as 25+ Vehicles Available and 10+ Premium Brands, while the
   supplied sample list contains six vehicles and three brands. Update
   these figures so they reflect the real inventory.
4. Currency and location: The app displays AUD prices and lists
   Queensland, Australia. Confirm these match the intended business.
5. Images: Vehicle and hero images are loaded from Unsplash URLs.
   Check that each image is appropriate for the vehicle listing and
   that you have the rights needed for commercial use.
6. Forms: Add actual submission handling, validation, privacy
   disclosures, and secure storage before collecting customer
   information.
7. Secrets and privacy: Do not place API keys, passwords, or other
   secrets directly in source code. Use Streamlit secrets or
   environment variables if integrations are added.
8. Testing: Test navigation, filters, vehicle detail buttons,
   WhatsApp links, and forms on desktop and mobile-sized screens.
Deployment
The app can be deployed to a hosting service that supports Streamlit.
For a typical deployment, include:
- app.py
- requirements.txt
A minimal requirements.txt is:
streamlit
Then configure the hosting service to run:
streamlit run app.py
Consult the Streamlit documentation for
current deployment instructions.
License
No license is specified in the supplied source code. Add a license file
if you intend to distri
