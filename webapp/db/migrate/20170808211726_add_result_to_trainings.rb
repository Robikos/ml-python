class AddResultToTrainings < ActiveRecord::Migration[5.0]
  def change
    add_column :trainings, :result, :string
  end
end
