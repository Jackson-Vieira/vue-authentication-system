<template>
  {{ message }}
</template>

<script lang="ts">
import { objectExpression } from "@babel/types";
import { defineComponent, ref } from "vue";
import { onMounted } from "vue";
import { useStore } from "vuex";

export default defineComponent({
  name: "HomeView",

  setup() {
    const accesstoken = localStorage.getItem("accesstoken");
    const store = useStore();
    /* The difference between ref and reactive, ref is for a single value, while, 
     reactive refer to an object and applied ref to each attribute in the object. */
    const message = ref("You are not logged in!");

    onMounted(async () => {
      try {
        const response = await fetch("http://localhost:8000/api/me/", {
          method: "GET",
          headers: {
            "Content-Type": "application/json",
            Authorization: `Bearer ${accesstoken}`,
          },
          credentials: "include",
        });

        const user = await response.json();
        console.log(user);
        if (user.username) {
          message.value = `Hello, ${user.username}`;
          await store.dispatch('setAuth', true)
        }
      } catch (error) {
        await store.dispatch('setAuth', false)
        console.log(error)
      }
    });

    return {
      message,
    };
  },
});
</script>

<style></style>
