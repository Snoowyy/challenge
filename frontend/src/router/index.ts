import { createRouter, createWebHistory, RouteRecordRaw } from "vue-router";
import ProductView from "../views/ProductView.vue";

const routes: Array<RouteRecordRaw> = [
  {
    path: "/product/:id",
    name: "ProductDetail",
    component: ProductView,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
