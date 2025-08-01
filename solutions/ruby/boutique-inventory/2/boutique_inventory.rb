# frozen_string_literal: true

# Boutique inventory exercise
class BoutiqueInventory
  def initialize(items)
    @items = items
  end

  def item_names = @items.map { _1[:name] }.sort

  def cheap = @items.select { _1[:price] < 30 }

  def out_of_stock = @items.select { _1[:quantity_by_size].empty? }

  def stock_for_item(name) = @items.find { _1[:name] == name }[:quantity_by_size]

  def total_stock = @items.map { _1[:quantity_by_size].values.sum }.sum
end
