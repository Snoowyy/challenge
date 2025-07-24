<template>
  <div class="highlights-container">
    <h2 class="section-title">Lo que tenés que saber de este producto</h2>
    <ul class="highlights-list">
      <li>
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 18H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2v2"/><path d="m21.5 17-1.1 1.1a1.5 1.5 0 0 1-2.1 0L17 17"/><path d="M15 19 12.5 22l-2.5-3"/><path d="m17 12 1.1 1.1a1.5 1.5 0 0 0 2.1 0L21.5 12"/><path d="m19 15-2.5-3-2.5 3"/></svg>
        <span>Desbloqueo facial y dactilar.</span>
      </li>
      <li>
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect width="18" height="18" x="3" y="3" rx="2"/><path d="M7 15h1a2 2 0 0 0 2-2V9a2 2 0 0 0-2-2H7"/><path d="M15 9h-2a2 2 0 0 0-2 2v2a2 2 0 0 0 2 2h2"/></svg>
        <span>Pantalla AMOLED de 6.67".</span>
      </li>
      <li>
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 13V7"/><path d="M12 17h.01"/><path d="M21 12a9 9 0 1 1-9-9 9.17 9.17 0 0 1 9 9Z"/></svg>
        <span>Tiene 3 cámaras traseras de 200Mpx/8Mpx/2Mpx.</span>
      </li>
    </ul>
  </div>
</template>

<style scoped>
.highlights-container {
  border-top: 1px solid #eee;
  padding-top: 24px;
}

.section-title {
  font-size: 20px;
  font-weight: 400;
  margin-bottom: 24px;
}

.highlights-list {
  list-style: none;
  padding: 0;
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.highlights-list li {
  display: flex;
  align-items: center;
  gap: 12px;
  font-size: 16px;
  color: #444;
}

.highlights-list svg {
  color: #666;
}
</style>