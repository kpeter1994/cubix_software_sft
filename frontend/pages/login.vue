<script lang="ts" setup>
  import { object, string } from "yup";
  import type { InferType } from "yup";

  const authStore = useAuthStore();

  definePageMeta({
    middleware: "already-logged-in"
  })

  useSeoMeta({
    title: "Log in",
    description: "Enter your email & password to log in.",
  });

  const LoginSchema = object({
    username: string().required().label("Felhasználónév"),
    password: string().required().label("Jelszó"),
  });

  const { handleSubmit, isSubmitting } = useForm<InferType<typeof LoginSchema>>({
    validationSchema: LoginSchema,
  });

  const submit = handleSubmit(async (values) => {

      const response : any = await authStore.login(values.username, values.password);

      const { error, message } = response;

      if (error) {
        useSonner.error(error);
        return;
      }

      useSonner.success(message);

      await navigateTo("/", { replace: true });

  });
</script>

<template>
  <div class="flex pt-6 lg:pt-12 items-center justify-center">
    <div class="w-full max-w-[330px] px-5">
      <h1 class="text-2xl font-bold tracking-tight lg:text-3xl">Log in</h1>
      <p class="mt-1 text-muted-foreground">Enter your email & password to log in.</p>


      <form class="mt-10" @submit="submit">
        <fieldset :disabled="isSubmitting" class="grid gap-5">
          <div>
            <UiVeeInput label="Email" type="text" name="username" placeholder="john@example.com" />
          </div>
          <div>
            <UiVeeInput label="Password" type="password" name="password" />
          </div>
          <div>
            <UiButton class="w-full" type="submit" text="Log in" />
          </div>
        </fieldset>
      </form>
      <p class="mt-8 text-sm">
        <NuxtLink class="font-semibold text-primary underline-offset-2 hover:underline" to="#"
        >Forgot password?</NuxtLink
        >
      </p>
      <p class="mt-4 text-sm text-muted-foreground">
        Don't have an account?
        <NuxtLink to="/register" class="font-semibold text-primary underline-offset-2 hover:underline"
        >Create account</NuxtLink
        >
      </p>
    </div>
  </div>
</template>

