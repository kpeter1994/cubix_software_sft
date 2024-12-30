<script setup lang="ts">

const authStore = useAuthStore();

const logout = () => {
  authStore.logout();

  navigateTo("/login", { replace: true });
};

</script>

<template>
    <UiNavbar>
      <UiContainer class="flex h-14 items-center justify-between">
        <NuxtLink to="/" class="font-semibold">Portfolio Manager</NuxtLink>
        <nav class="hidden items-center gap-5 sm:flex">
         <NuxtLink to="/" class="hover:underline">Home</NuxtLink>
         <NuxtLink v-if="!authStore.isLogedIn" to="/login" class="hover:underline">Login</NuxtLink>
         <UiButton v-if="authStore.isLogedIn" @click="logout">Log out</UiButton>
        </nav>
      </UiContainer>
    </UiNavbar>
    <slot />
</template>

<style scoped></style>
