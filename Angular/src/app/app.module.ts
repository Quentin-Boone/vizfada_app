import { BrowserModule } from '@angular/platform-browser';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { NgModule, CUSTOM_ELEMENTS_SCHEMA } from '@angular/core';
import { HttpClientModule, HttpClientXsrfModule, HTTP_INTERCEPTORS } from '@angular/common/http';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { FlexLayoutModule } from '@angular/flex-layout';
import { IconsModule } from './icons/icons.module';
import { DragDropModule } from '@angular/cdk/drag-drop';
import { RouterModule } from '@angular/router';
import { ObserversModule } from "@angular/cdk/observers";

import * as PlotlyJS from 'plotly.js-dist/plotly.js';
import { PlotlyModule } from 'angular-plotly.js';
import { NgMultiSelectDropDownModule } from 'ng-multiselect-dropdown';
import { ColorPickerModule } from 'ngx-color-picker';
import { NgxSpinnerModule } from "ngx-spinner";
import { NgxFilesizeModule } from 'ngx-filesize';
import { NgxDatatableModule } from '@swimlane/ngx-datatable';

import { AppComponent } from './app.component';
import { ControllerComponent } from './main/controller/controller.component';
import { HeatmapComponent } from './main/view/heatmap/heatmap.component';
import { FilterComponent } from './main/controller/filter/filter.component';
import { HighlightComponent } from './main/controller/highlight/highlight.component';
import { LegendComponent } from './main/view/heatmap/legend/legend.component';
import { ViewComponent } from './main/view/view.component';
import { MainComponent } from './main/main.component';
import { CanvasComponent } from './main/view/heatmap/canvas/canvas.component';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';

import { HeaderComponent } from './header/header.component';
import { AboutComponent } from './about/about.component';

import { PlotlyComponent } from './main/view/heatmap/plotly/plotly.component';
import { SafeHTMLPipe } from './main/safe-html.pipe';

import { ExperimentComponent } from './experiments/experiment/experiment.component';
import { ExperimentsListComponent } from './experiments/experiments-list/experiments-list.component';
import { MetadataTableComponent } from './main/metadata-table/metadata-table.component';
import { SafePipe } from './safe.pipe';
import { BetterNamesPipe } from './better-names.pipe';
import { GetPipe } from './get.pipe';
import { CarouselComponent } from './epistack/carousel/carousel.component';
import { EpistackComponent } from './epistack/epistack.component';
import { MenuComponent } from './epistack/menu/menu.component';
import { TestComponent } from './main/test/test.component';
import { CsrfInterceptor } from './utils/csrf-interceptor'

PlotlyModule.plotlyjs = PlotlyJS;

@NgModule({
  declarations: [
    AboutComponent,
    AppComponent,
    BetterNamesPipe,
    CanvasComponent,
    ControllerComponent,
    ExperimentComponent,
    ExperimentsListComponent,
    FilterComponent,
    HeaderComponent,
    HeatmapComponent,
    HighlightComponent,
    LegendComponent,
    MainComponent,
    MetadataTableComponent,
    PlotlyComponent,
    SafeHTMLPipe,
    SafePipe,
    ViewComponent,
    GetPipe,
    CarouselComponent,
    EpistackComponent,
    MenuComponent,
    TestComponent,
  ],
  imports: [
    BrowserAnimationsModule,
    BrowserModule,
    ColorPickerModule,
    DragDropModule,
    FlexLayoutModule,
    FormsModule,
    HttpClientModule,
    HttpClientXsrfModule,
    IconsModule,
    NgbModule,
    NgMultiSelectDropDownModule,
    NgxDatatableModule,
    NgxFilesizeModule,
    NgxSpinnerModule,
    ObserversModule,
    PlotlyModule,
    ReactiveFormsModule,
    RouterModule.forRoot([
      { path: '', component: MainComponent },
      { path: 'about', component: AboutComponent },
      { path: 'experiments', component: ExperimentsListComponent },
      { path: 'experiment/:id', component: ExperimentComponent },
      { path: 'epistack', component: EpistackComponent }
    ]),
  ],
  bootstrap: [AppComponent],
  schemas: [CUSTOM_ELEMENTS_SCHEMA],
})
export class AppModule {
  constructor() {
  }
}
