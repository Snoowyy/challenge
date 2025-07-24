<template>
  <teleport to="body">
    <div class="modal-backdrop" @click="$emit('close')">
      <div class="modal-content" @click.stop>
        <header class="modal-header">
          <h3>Medios de pago para este producto</h3>
          <button @click="$emit('close')" class="close-button">×</button>
        </header>

        <main class="modal-body">
          <div class="mercado-pago-section">
            <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSHZqj-XReJ2R76nji51cZl4ETk6-eHRmZBRw&s" alt="Mercado Pago">
            <p>Pagar con <strong>Mercado Pago</strong> es elegir cualquiera de estos medios. Es rápido, seguro y no tiene costo adicional.</p>
          </div>
          
          <div class="payment-category">
            <h4>Tarjetas de crédito</h4>
            <p class="subtitle">Acreditación instantánea.</p>
            
            <p class="interest-info"><strong>Hasta 12 cuotas con 0% interés</strong> con estos bancos</p>
            <div class="logo-grid">
              <div v-for="bank in interestFreeBanks" :key="bank.name" class="bank-item">
                <img :src="bank.logoUrl" :alt="bank.name">
                <span>{{ bank.installments }} cuotas</span>
              </div>
            </div>

            <p class="interest-info">O hasta 48 cuotas con interés</p>
            <div class="logo-grid">
              <div v-for="card in withInterestCards" :key="card.name" class="bank-item">
                <img :src="card.logoUrl" :alt="card.name">
                <span>{{ card.installments }} cuotas</span>
              </div>
            </div>
          </div>
          
          <div class="payment-category">
            <h4>Tarjetas de débito</h4>
            <p class="subtitle">Acreditación instantánea.</p>
            <div class="logo-grid debit-grid">
               <div v-for="card in debitCards" :key="card.name" class="bank-item">
                <img :src="card.logoUrl" :alt="card.name">
              </div>
            </div>
          </div>

        </main>
      </div>
    </div>
  </teleport>
</template>

<script setup lang="ts">
defineEmits(['close']);

const interestFreeBanks = [
  { name: 'Bancolombia', logoUrl: 'https://i.pinimg.com/564x/b8/cd/c1/b8cdc1ad498fe080bc21bb5a03c24f83.jpg', installments: 12 },
  { name: 'Av Villas', logoUrl: 'https://cosmocentro.com/wp-content/uploads/2017/01/LOGO-AV-VILLAS-CON-CONTENEDOR.png', installments: 12 },
  { name: 'Banco de Bogotá', logoUrl: 'https://oldprovidence.co/wp-content/uploads/2024/08/banco-de-bogota-logo.png', installments: 12 },
  { name: 'BBVA', logoUrl: 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/BBVA_2019.svg/1280px-BBVA_2019.svg.png', installments: 12 },
];

const withInterestCards = [
  { name: 'Codensa', logoUrl: 'https://cdn.aglty.io/scotiabank-colombia/CodensaAssets/logos-codensa/logo05.png', installments: 48 },
  { name: 'Visa', logoUrl: 'https://img.icons8.com/?size=100&id=1429&format=png&color=000000', installments: 36 },
  { name: 'Mastercard', logoUrl: 'https://cdn.worldvectorlogo.com/logos/mastercard-7.svg', installments: 36 },
  { name: 'American Express', logoUrl: 'https://img.icons8.com/?size=100&id=1433&format=png&color=000000', installments: 36 },
  { name: 'Diners Club', logoUrl: 'https://cdn-icons-png.flaticon.com/512/196/196548.png', installments: 36 },
];

const debitCards = [
  { name: 'Visa Débito', logoUrl: 'https://cdn.pixabay.com/photo/2021/12/06/13/48/visa-6850402_1280.png' },
  { name: 'Mastercard Débito', logoUrl: 'https://upload.wikimedia.org/wikipedia/commons/thumb/b/b7/MasterCard_Logo.svg/2560px-MasterCard_Logo.svg.png' }
];

</script>

<style scoped>
.modal-backdrop {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  background-color: rgba(0, 0, 0, 0.6);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
}

.modal-content {
  background-color: white;
  border-radius: 8px;
  width: 90%;
  max-width: 680px;
  max-height: 90vh;
  display: flex;
  flex-direction: column;
}

.modal-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem 1.5rem;
  border-bottom: 1px solid #eee;
}

.modal-header h3 {
  margin: 0;
  font-size: 1.25rem;
}

.close-button {
  background: none;
  border: none;
  font-size: 2rem;
  line-height: 1;
  cursor: pointer;
  color: #888;
}

.modal-body {
  padding: 1.5rem;
  overflow-y: auto;
  font-family: Arial, sans-serif;
}

.mercado-pago-section {
  display: flex;
  align-items: center;
  gap: 1rem;
  margin-bottom: 2rem;
}
.mercado-pago-section img { height: 30px; }
.mercado-pago-section p { margin: 0; color: #555; }

.payment-category {
  border-top: 1px solid #eee;
  padding-top: 1.5rem;
  margin-top: 1.5rem;
}

.payment-category h4 {
  font-size: 1.1rem;
  margin: 0 0 0.25rem 0;
}

.subtitle {
  font-size: 0.9rem;
  color: #777;
  margin: 0 0 1.5rem 0;
}

.interest-info {
  font-size: 1rem;
  margin: 1.5rem 0 1rem 0;
}

.logo-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(120px, 1fr));
  gap: 1.5rem;
}

.debit-grid {
  grid-template-columns: repeat(auto-fill, minmax(100px, 1fr));
}

.bank-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
}

.bank-item img {
  height: 35px;
  margin-bottom: 0.5rem;
  object-fit: contain;
}

.bank-item span {
  font-size: 0.8rem;
  color: #777;
}
</style>