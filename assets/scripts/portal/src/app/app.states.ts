import { LoginComponent } from 'app/components/login/login.component';
import { AppComponent } from 'app/app.component';

export const appState = {
  name: 'app',
  component: AppComponent,
};

export const loginState = {
  name : 'app.login',
  url: '/',
  views : {
    'content@app' : {
      component: LoginComponent,
      }
  }
};

export const APP_STATES = [
    appState,
    loginState,
]