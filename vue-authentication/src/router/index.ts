import { createRouter, createWebHistory, RouteRecordRaw } from "vue-router";
import Home from '../views/HomeView.vue'
import Login from '../views/LoginView.vue'
import Register from '../views/RegisterView.vue'
import { canUserAccess } from '../utils/canUserAccess'


const routes: Array<RouteRecordRaw> = [
  {path: "/", name: 'home',component: Home},
  {path: "/signin", name: 'signin', component: Login},
  {path: "/signup", name: 'signup', component: Register},
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});


router.beforeEach(async (to, from) => {
  // canUserAccess() returns `true` or `false`
  const canAccess = await canUserAccess();
  if(to.name === "home" && !canAccess) return '/signin'
})


export default router;
