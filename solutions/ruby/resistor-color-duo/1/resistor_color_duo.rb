# Return the value of a resistor based on the first two bands
module ResistorColorDuo
  COLORS = %w[black brown red orange yellow green blue violet grey white].each_with_index.to_h

  def self.value(bands) = (COLORS[bands[0]] * 10) + COLORS[bands[1]]
end
