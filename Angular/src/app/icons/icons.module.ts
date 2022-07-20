import { NgModule } from '@angular/core';
import { BootstrapIconsModule } from 'ng-bootstrap-icons';
import { ChevronDown, ChevronUp, Download, Folder2, Folder2Open, Funnel, FunnelFill, PaletteFill, Trash, TrashFill } from 'ng-bootstrap-icons/icons';


const icons = {
  ChevronDown,
  ChevronUp,
  Download,
  Funnel,
  FunnelFill,
  PaletteFill,
  Trash,
  TrashFill,
  Folder2,
  Folder2Open
};

@NgModule({
  declarations: [],
  imports: [
    BootstrapIconsModule.pick(icons)
  ], exports: [
    BootstrapIconsModule
  ]
})
export class IconsModule { }
