<script setup lang="ts"></script>

<template>
  <div>
    <UiNavbar>
      <UiContainer class="flex h-14 items-center justify-between border border-b-0">
        <NuxtLink to="/" class="font-semibold">Portfolio Manager</NuxtLink>
        <nav class="hidden items-center gap-5 sm:flex">
         <NuxtLink to="/" class="hover:underline">Home</NuxtLink>
         <NuxtLink to="/login" class="hover:underline">Login</NuxtLink>
        </nav>
      </UiContainer>
    </UiNavbar>
    <slot />
  </div>
</template>

<style scoped></style>
