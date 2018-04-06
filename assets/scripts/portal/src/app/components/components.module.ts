import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { LoginComponent } from 'app/components/login/login.component';
import { UIRouterModule } from '@uirouter/angular';

@NgModule({
  imports: [
    CommonModule,
    UIRouterModule,
  ],
  declarations: [
    LoginComponent,
    ]
})
export class ComponentsModule { }
