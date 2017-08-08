class TrainingsController < ApplicationController
  def index
  end

  def new
    @training = Training.new
  end

  def create
    @training = Training.new(training_params)
    if @training.save
      TrainingProducer.publish(
        data: @training.data,
        result: @training.result
      )

      redirect_to trainings_path, notice: "Train added successfully"
    else
      redirect_to trainings_path, alert: "Error while adding train"
    end
  end

  private

  def training_params
    params.require(:training).permit(:data, :result)
  end
end
