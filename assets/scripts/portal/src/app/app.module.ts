import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { UIRouterModule, UIView } from '@uirouter/angular';
import { APP_STATES } from 'app/app.states';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import { AppComponent } from './app.component';

import { ComponentsModule } from 'app/components/components.module';

@NgModule({
  declarations: [
    AppComponent,
  ],
  imports: [
    UIRouterModule.forRoot({
      states: APP_STATES,
      useHash: false,
      otherwise: '/not-found',
    }),
    BrowserModule,
    ComponentsModule,
    NgbModule,
  ],
  providers: [],
  bootstrap: [UIView]
})
export class AppModule { }
