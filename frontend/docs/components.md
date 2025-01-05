# Frontend Components Documentation

This document provides an overview of the frontend components used in the project. Each component is described with its purpose, usage, and examples.

## Components

### AddStock.vue

**Purpose:**  
The `AddStock.vue` component is used to add a new stock to the portfolio.

**Usage:**  
The component is used within the application to allow users to input stock details and add them to their portfolio.

**Example:**
```vue
<template>
  <AddStock />
</template>
```

### ChartComponent.vue

**Purpose:**  
The `ChartComponent.vue` component is used to display stock price history in a candlestick chart.

**Usage:**  
The component fetches stock price data and displays it in a chart format.

**Example:**
```vue
<template>
  <ChartComponent />
</template>
```

### Accordion.vue

**Purpose:**  
The `Accordion.vue` component is used to create an accordion interface.

**Usage:**  
The component is used to display collapsible content sections.

**Example:**
```vue
<template>
  <Accordion :items="accordionItems" />
</template>
```

### Alert.vue

**Purpose:**  
The `Alert.vue` component is used to display alert messages.

**Usage:**  
The component is used to show different types of alert messages such as success, error, info, and warning.

**Example:**
```vue
<template>
  <Alert variant="success" title="Success" description="Operation completed successfully." />
</template>
```

### Button.vue

**Purpose:**  
The `Button.vue` component is used to create buttons.

**Usage:**  
The component is used to create various types of buttons with different styles and functionalities.

**Example:**
```vue
<template>
  <Button @click="handleClick">Click Me</Button>
</template>
```

### Input.vue

**Purpose:**  
The `Input.vue` component is used to create input fields.

**Usage:**  
The component is used to create various types of input fields such as text, password, and number.

**Example:**
```vue
<template>
  <Input v-model="inputValue" placeholder="Enter text" />
</template>
```

### Modal.vue

**Purpose:**  
The `Modal.vue` component is used to create modal dialogs.

**Usage:**  
The component is used to display modal dialogs with customizable content.

**Example:**
```vue
<template>
  <Modal v-model:open="isModalOpen">
    <template #header>
      <h3>Modal Title</h3>
    </template>
    <template #body>
      <p>Modal content goes here.</p>
    </template>
    <template #footer>
      <Button @click="isModalOpen = false">Close</Button>
    </template>
  </Modal>
</template>
```

### Table.vue

**Purpose:**  
The `Table.vue` component is used to create tables.

**Usage:**  
The component is used to display data in a tabular format.

**Example:**
```vue
<template>
  <Table :data="tableData" :columns="tableColumns" />
</template>
```

### Tabs.vue

**Purpose:**  
The `Tabs.vue` component is used to create tabbed interfaces.

**Usage:**  
The component is used to display content in a tabbed format.

**Example:**
```vue
<template>
  <Tabs>
    <Tab title="Tab 1">Content for Tab 1</Tab>
    <Tab title="Tab 2">Content for Tab 2</Tab>
  </Tabs>
</template>
```

### Toast.vue

**Purpose:**  
The `Toast.vue` component is used to display toast notifications.

**Usage:**  
The component is used to show brief messages that disappear automatically.

**Example:**
```vue
<template>
  <Toast variant="info" title="Info" description="This is an info toast." />
</template>
```

### Tooltip.vue

**Purpose:**  
The `Tooltip.vue` component is used to display tooltips.

**Usage:**  
The component is used to show additional information when hovering over an element.

**Example:**
```vue
<template>
  <Tooltip content="This is a tooltip">
    <Button>Hover me</Button>
  </Tooltip>
</template>
```

## Conclusion

This document provides an overview of the frontend components used in the project. Each component is described with its purpose, usage, and examples. For more detailed information, refer to the component's source code and documentation.
