# Frontend Stores Documentation

This document provides an overview of the frontend stores used in the project. Each store is described with its purpose, usage, and examples.

## Stores

### auth.ts

**Purpose:**  
The `auth.ts` store is used to manage user authentication state.

**Usage:**  
The store provides methods for user registration, login, logout, and token verification.

**Example:**
```typescript
import { useAuthStore } from '~/stores/auth';

const authStore = useAuthStore();

// Register a new user
authStore.register({ name: 'John Doe', username: 'john', password: 'password123' });

// Login a user
authStore.login('john', 'password123');

// Logout the user
authStore.logout();
```

### portfolio.ts

**Purpose:**  
The `portfolio.ts` store is used to manage user portfolios.

**Usage:**  
The store provides methods for creating, deleting, and fetching portfolios, as well as adding and removing shares from portfolios.

**Example:**
```typescript
import { usePortfolioStore } from '~/stores/portfolio';

const portfolioStore = usePortfolioStore();

// Create a new portfolio
portfolioStore.createPortfolio('My Portfolio', 'This is my portfolio description.');

// Get all portfolios
portfolioStore.getAllPortfolios();

// Delete a portfolio
portfolioStore.deletePortfolio(1);

// Add shares to a portfolio
portfolioStore.addSharesToPortfolio(1, { symbol: 'AAPL', quantity: 10 });
```

### stock.ts

**Purpose:**  
The `stock.ts` store is used to manage stock data.

**Usage:**  
The store provides methods for setting the current stock and fetching stock data.

**Example:**
```typescript
import { useStockStore } from '~/stores/stock';

const stockStore = useStockStore();

// Set the current stock
stockStore.setStock('AAPL');

// Get the current stock data
stockStore.getShareActualData('AAPL');
```

## Conclusion

This document provides an overview of the frontend stores used in the project. Each store is described with its purpose, usage, and examples. For more detailed information, refer to the store's source code and documentation.
