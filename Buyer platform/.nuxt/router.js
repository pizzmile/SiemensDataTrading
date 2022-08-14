import Vue from 'vue'
import Router from 'vue-router'
import { normalizeURL, decode } from 'ufo'
import { interopDefault } from './utils'
import scrollBehavior from './router.scrollBehavior.js'

const _7d17906a = () => interopDefault(import('../pages/purchase.vue' /* webpackChunkName: "pages/purchase" */))
const _0adce68c = () => interopDefault(import('../pages/settings.vue' /* webpackChunkName: "pages/settings" */))
const _0a7bcab9 = () => interopDefault(import('../pages/index.vue' /* webpackChunkName: "pages/index" */))

const emptyFn = () => {}

Vue.use(Router)

export const routerOptions = {
  mode: 'history',
  base: '/',
  linkActiveClass: 'nuxt-link-active',
  linkExactActiveClass: 'nuxt-link-exact-active',
  scrollBehavior,

  routes: [{
    path: "/purchase",
    component: _7d17906a,
    name: "purchase"
  }, {
    path: "/settings",
    component: _0adce68c,
    name: "settings"
  }, {
    path: "/",
    component: _0a7bcab9,
    name: "index"
  }, {
    path: "/home",
    component: _0a7bcab9,
    name: "home"
  }],

  fallback: false
}

export function createRouter (ssrContext, config) {
  const base = (config._app && config._app.basePath) || routerOptions.base
  const router = new Router({ ...routerOptions, base  })

  // TODO: remove in Nuxt 3
  const originalPush = router.push
  router.push = function push (location, onComplete = emptyFn, onAbort) {
    return originalPush.call(this, location, onComplete, onAbort)
  }

  const resolve = router.resolve.bind(router)
  router.resolve = (to, current, append) => {
    if (typeof to === 'string') {
      to = normalizeURL(to)
    }
    return resolve(to, current, append)
  }

  return router
}
