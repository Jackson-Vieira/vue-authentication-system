<template>
  <nav class="d-flex p-2 justify-content-between align-items-center" style="color: black">
    <router-link to="/">Home</router-link>
    <div v-if="!auth" style="display: flex; flex-direction: row; gap: 20px; margin-right: 50px;">
        <router-link to="/signin">Login</router-link>
        <router-link to="/signup">Register</router-link>
    </div>
      <a v-else  @click.prevent="logout"  href="" style="color: red">Logout</a>
  </nav>
</template> 

<script lang="ts">
import {computed} from 'vue';
import { useRouter } from 'vue-router';
  import { useStore } from 'vuex';

  export default {
    name: "NavBar",
    setup(){
      const store = useStore()
      const router = useRouter()
      const auth = computed( () => store.state.authenticated)

      const logout =  async () => {
         localStorage.removeItem("accesstoken");
         await store.dispatch('setAuth', false)
         router.push('/signin')
      }

      return {
        auth,
        logout
      }
    }
  }
</script>


<style>
  nav {
    display: block;
  }

</style>