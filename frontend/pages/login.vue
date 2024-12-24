<template>
  <div class="flex h-screen items-center justify-center">
    <div class="w-full max-w-[330px] px-5">
      <h1 class="text-2xl font-bold tracking-tight lg:text-3xl">Log in</h1>
      <p class="mt-1 text-muted-foreground">Enter your username & password to log in.</p>

      <form class="mt-10" @submit.prevent="submit">
        <fieldset :disabled="isSubmitting" class="grid gap-5">
          <div>
            <UiVeeInput label="Username" type="text" v-model="username" placeholder="john_doe" />
          </div>
          <div>
            <UiVeeInput label="Password" type="password" v-model="password" />
          </div>
          <div>
            <UiButton class="w-full" type="submit" text="Log in" />
          </div>
        </fieldset>
      </form>
      <p class="mt-8 text-sm">
        <NuxtLink class="font-semibold text-primary underline-offset-2 hover:underline" to="#"
        >Forgot password?</NuxtLink>
      </p>
      <p class="mt-4 text-sm text-muted-foreground">
        Don't have an account?
        <NuxtLink class="font-semibold text-primary underline-offset-2 hover:underline" to="#"
        >Create account</NuxtLink>
      </p>
    </div>
  </div>
</template>

<script lang="ts" setup>
import { ref } from "vue";

useSeoMeta({
  title: "Log in",
  description: "Enter your username & password to log in.",
});

// Form fields
const username = ref("");
const password = ref("");
const isSubmitting = ref(false);

const submit = async () => {
  isSubmitting.value = true;

  try {
    const response = await fetch("http://localhost:5000/login", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        username: username.value,
        password: password.value,
      }),
    });

    if (response.ok) {
      const data = await response.json();
      alert("Logged in successfully: " + data.message);
      // Például átirányítás másik oldalra
      // router.push("/dashboard");
    } else {
      const errorData = await response.json();
      alert("Login failed: " + (errorData.message || "Invalid credentials"));
    }
  } catch (error) {
    alert("A network error occurred. Please try again later.");
  } finally {
    isSubmitting.value = false;
  }
};
</script>
