//Form.vue

<template>
  <div>
    <h4 class="text-center">Login-techlab-board</h4>
    <form @submit.prevent="loginSubmit" novalidate>
 
      <div class="form-group">
        <label for="email">{{ $t('form.email') }} *</label>
        <input type="email" class="form-control" id="email" v-model.lazy.trim="form.email" @blur="onFieldBlur('email')" v-bind:class="getFieldClasses('email')">
        <div v-if="isErrorField('email')" class="invalid-feedback">{{ $t('error.fieldInvalid', { field: $t('form.email') }) }}</div>
      </div>

      <div class="alert alert-danger" v-if="loginError">
        <p class="mb-0">
          <strong>{{ $t(errorHeader) }}</strong>
        </p>
        <ul class="mb-0 pl-3" v-if="errors.length > 0">
          <li v-for="error in errors" v-bind:key="error.field">
            <span v-if="error.field">{{ $t('form.'+error.field) }}<span v-if="error.message">: {{ $t(error.message) }}</span></span>
            <span v-else-if="error.message">{{ $t(error.message) }}</span>
          </li>
        </ul>
      </div>
      <div class="form-group">
        <button type="submit" class="btn btn-success" :disabled="loggingIn">
          <span v-if="loggingIn">{{ $t('form.loggingIn') }} <img src="../../assets/loader.svg" /></span>
          <span v-else>{{ $t('form.submit') }}</span>
        </button>
      </div>
    </form>
  </div>
</template>

<script src="./Form.js"></script>
<style src="./Form.sass" lang="sass" scoped></style>
