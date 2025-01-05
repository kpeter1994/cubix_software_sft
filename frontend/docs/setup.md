# Frontend Setup Instructions

## Prerequisites

Before setting up the frontend environment, ensure you have the following installed:

- Node.js (version 14 or higher)
- npm (Node Package Manager)

## Setup Steps

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install dependencies:**
   ```bash
   npm install
   ```

3. **Create a `.env` file:**
   In the `frontend` directory, create a `.env` file and add the following environment variables:
   ```env
   BACKEND_URL=http://127.0.0.1:5000
   ```

4. **Start the development server:**
   ```bash
   npm run dev
   ```

## Required Dependencies and Configurations

- **Node.js:** Ensure you have Node.js installed. You can download it from [nodejs.org](https://nodejs.org/).
- **npm:** npm is included with Node.js. Verify the installation by running `npm -v` in your terminal.
- **Environment Variables:** The `.env` file should contain the `BACKEND_URL` variable pointing to your backend server.

## Additional Notes

- If you encounter any issues during setup, refer to the project's `README.md` file for troubleshooting tips.
- Ensure your backend server is running and accessible at the URL specified in the `BACKEND_URL` variable.
