# Composables Documentation

## Purpose and Usage

### useApiFetch

**Purpose**: A composable function to make API requests with authentication.

**Usage**:
```typescript
import { useApiFetch } from '~/composables/useApiFetch';

const data = await useApiFetch('/api/path', { method: 'GET' });
```

### useCarousel

**Purpose**: A composable function to manage carousel functionality.

**Usage**:
```typescript
import { useCarousel, useProvideCarousel } from '~/composables/useCarousel';

const { carouselRef, scrollNext, scrollPrev } = useCarousel();
```

### useFormField

**Purpose**: A composable function to manage form field state and validation.

**Usage**:
```typescript
import { useFormField } from '~/composables/useFormField';

const { name, error, isDirty, isTouched, valid } = useFormField();
```

### useToast

**Purpose**: A composable function to manage toast notifications.

**Usage**:
```typescript
import { useToast, toast } from '~/composables/useToast';

const { toasts, dismiss } = useToast();
toast({ title: 'Success', description: 'Operation completed successfully' });
```

## Examples

### Example of useApiFetch
```typescript
import { useApiFetch } from '~/composables/useApiFetch';

const fetchData = async () => {
  try {
    const data = await useApiFetch('/api/data');
    console.log(data);
  } catch (error) {
    console.error('Error fetching data:', error);
  }
};
```

### Example of useCarousel
```typescript
import { useCarousel, useProvideCarousel } from '~/composables/useCarousel';

export default {
  setup() {
    const { carouselRef, scrollNext, scrollPrev } = useCarousel();

    return {
      carouselRef,
      scrollNext,
      scrollPrev,
    };
  },
};
```

### Example of useFormField
```typescript
import { useFormField } from '~/composables/useFormField';

export default {
  setup() {
    const { name, error, isDirty, isTouched, valid } = useFormField();

    return {
      name,
      error,
      isDirty,
      isTouched,
      valid,
    };
  },
};
```

### Example of useToast
```typescript
import { useToast, toast } from '~/composables/useToast';

export default {
  setup() {
    const { toasts, dismiss } = useToast();

    const showToast = () => {
      toast({ title: 'Success', description: 'Operation completed successfully' });
    };

    return {
      toasts,
      dismiss,
      showToast,
    };
  },
};
```
