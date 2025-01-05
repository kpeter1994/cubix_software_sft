# Nuxt Minimal Starter

Look at the [Nuxt documentation](https://nuxt.com/docs/getting-started/introduction) to learn more.

## Setup

Make sure to install dependencies:

```bash
# npm
npm install

# pnpm
pnpm install

# yarn
yarn install

# bun
bun install
```

## Development Server

Start the development server on `http://localhost:3000`:

```bash
# npm
npm run dev

# pnpm
pnpm dev

# yarn
yarn dev

# bun
bun run dev
```

## Production

Build the application for production:

```bash
# npm
npm run build

# pnpm
pnpm build

# yarn
yarn build

# bun
bun run build
```

Locally preview production build:

```bash
# npm
npm run preview

# pnpm
pnpm preview

# yarn
yarn preview

# bun
bun run preview
```

Check out the [deployment documentation](https://nuxt.com/docs/getting-started/deployment) for more information.

## Frontend Developer Documentation

### Setup Instructions

To set up the frontend environment, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/kpeter1994/cubix_software_sft.git>
   cd https://github.com/kpeter1994/cubix_software_sft.git
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Create a `.env` file in the `frontend` directory and add the following environment variables:
   ```env
   BACKEND_URL=http://127.0.0.1:5000
   ```

4. Start the development server:
   ```bash
   npm run dev
   ```

### Working with Frontend Components, Composables, and Stores

#### Components

Components are located in the `frontend/components` directory. Each component should have a clear purpose and be reusable. To create a new component, follow these steps:

1. Create a new file in the appropriate subdirectory within `frontend/components`.
2. Define the component using the Vue 3 Composition API.
3. Add any necessary props, emits, and slots.
4. Document the component's purpose and usage in the `frontend/docs/components.md` file.

#### Composables

Composables are located in the `frontend/composables` directory. They are used to encapsulate reusable logic. To create a new composable, follow these steps:

1. Create a new file in the `frontend/composables` directory.
2. Define the composable function using the Vue 3 Composition API.
3. Document the composable's purpose and usage in the `frontend/docs/composables.md` file.

#### Stores

Stores are managed using Pinia and are located in the `frontend/stores` directory. To create a new store, follow these steps:

1. Create a new file in the `frontend/stores` directory.
2. Define the store using the Pinia API.
3. Document the store's purpose and usage in the `frontend/docs/stores.md` file.

### Frontend Build Process and Deployment

#### Build Process

To build the frontend application for production, run the following command:

```bash
npm run build
```

This will generate the production-ready files in the `.output` directory.

#### Deployment

To deploy the frontend application, follow these steps:

1. Build the application:
   ```bash
   npm run build
   ```

2. Copy the contents of the `.output` directory to your web server's root directory.

3. Ensure that the `BACKEND_URL` environment variable is set correctly on the server.

4. Start the application using a process manager like PM2 or a web server like Nginx.

For more detailed instructions, refer to the `frontend/docs/build-and-deploy.md` file.
