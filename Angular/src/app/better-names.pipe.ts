import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
  name: 'betterNames'
})
export class BetterNamesPipe implements PipeTransform {

  transform(value: string): string {
    switch (value) {
      case 'Bos_taurus': return "cow";
      case 'Capra_hircus': return "goat";
      case 'Equus_caballus': return "horse";
      case 'Gallus_gallus': return "chicken";
      case 'Ovis_aries': return 'sheep';
      case 'Sus_scrofa': return "pig";
      default: return value;
    }
  }

}
