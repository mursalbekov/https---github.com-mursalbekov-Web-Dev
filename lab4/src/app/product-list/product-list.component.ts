<<<<<<< HEAD
import { Component, Input } from '@angular/core';

import { Product, products } from '../products';
=======
import { Component } from '@angular/core';

import { products } from '../products';
>>>>>>> dfa4b5b1c40a1a5bb10ccf20916a5c82b2c6b7ae

@Component({
  selector: 'app-product-list',
  templateUrl: './product-list.component.html',
  styleUrls: ['./product-list.component.css']
})

export class ProductListComponent {
<<<<<<< HEAD
  products = [...products]
  @Input() categoryName: string | undefined;
  remove(id:number){
    this.products = this.products.filter((x) => x.id !== id);
  }
  share(product: Product) {
    window.alert('The product has been shared!');
  }
=======
  products = [...products];

  share() {
    window.alert('The product has been shared!');
  }

>>>>>>> dfa4b5b1c40a1a5bb10ccf20916a5c82b2c6b7ae
  onNotify() {
    window.alert('You will be notified when the product goes on sale');
  }
}
<<<<<<< HEAD
=======


/*
Copyright Google LLC. All Rights Reserved.
Use of this source code is governed by an MIT-style license that
can be found in the LICENSE file at https://angular.io/license
*/
>>>>>>> dfa4b5b1c40a1a5bb10ccf20916a5c82b2c6b7ae
