class TrainingsController < ApplicationController
  def index
  end

  def new
    @training = Training.new
  end

  def create
    @training = Training.new(training_params)
    if @training.save
      MessagesProducer.publish(trainings_hash)
      redirect_to trainings_path, notice: "Training added successfully"
    else
      redirect_to trainings_path, alert: "Error while adding traininig"
    end
  end

  private

  def training_params
    params.require(:training).permit(:data, :result)
  end

  def trainings_hash
    Training.select(:data, :result).to_json
  end
end
