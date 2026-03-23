# Trendsee Frontend (Vue 3 + Vite + Pinia + Router)

## Ideal Structure Implemented
```
src/
├── assets/         # Styles, images
├── types/          # TS interfaces (post.ts)
├── composables/    # Hooks (useApi.ts)
├── stores/         # Pinia (posts.ts)
├── router/         # Vue Router
├── pages/          # Route views (Home.vue)
├── layouts/        # Layouts (DefaultLayout.vue)
├── components/     # common/, ui/
├── App.vue         # Root
└── main.ts
```

## Setup
```bash
cd frontend
npm install
npm run dev  # http://localhost:5173
```

## Features
- Reels grid (Pinia store, mock data)
- Sidebar nav
- API ready (/posts → localhost:8000)
- Load more (demo fetch)
- TypeScript, responsive grid

## Build
```bash
npm run build
```

Backend: Run on :8000 for /api/posts integration.

