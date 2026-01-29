package InventoryManagement;

use 5.038;

sub create_inventory ($items) {
    my %inventory;
    $inventory{$_}++ foreach @$items;
    return \%inventory;
}

sub add_items ( $inventory, $items ) {
    $inventory->{$_}++ foreach @$items;
    return $inventory;
}

sub remove_items ( $inventory, $items ) {
    foreach (@$items) { $inventory->{$_}-- if $inventory->{$_} > 0; }
    return $inventory;
}

sub delete_item ( $inventory, $item ) {
    delete $inventory->{$item};
    return $inventory;
}

1;
