# frozen_string_literal: true

# Warning: OpenStruct is now officially discouraged
# See https://docs.ruby-lang.org/en/3.4/OpenStruct.html#class-OpenStruct-label-Caveats
require 'ostruct'

# Boutique inventory improvement exercise
class BoutiqueInventory
  attr_reader :items

  def initialize(items)
    @items = items.map(&OpenStruct.method(:new)) # rubocop:disable Style/OpenStructUse
  end

  def item_names = @items.map(&:name).sort

  def total_stock = @items.sum { _1.quantity_by_size.values.sum }
end
