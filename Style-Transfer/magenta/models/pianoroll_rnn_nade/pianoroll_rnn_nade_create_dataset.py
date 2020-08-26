# Copyright 2020 The Magenta Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Create a dataset of SequenceExamples from NoteSequence protos.

This script will extract pianoroll tracks from NoteSequence protos and save
them to TensorFlow's SequenceExample protos for input to the RNN-NADE checkpoint.
"""

import os

from magenta.models.pianoroll_rnn_nade import pianoroll_rnn_nade_model
from magenta.pipelines import pianoroll_pipeline
from magenta.pipelines import pipeline
import tensorflow.compat.v1 as tf

flags = tf.app.flags
FLAGS = tf.app.flags.FLAGS
flags.DEFINE_string(
    'input', None,
    'TFRecord to read NoteSequence protos from.')
flags.DEFINE_string(
    'output_dir', None,
    'Directory to write training and eval TFRecord files. The TFRecord files '
    'are populated with SequenceExample protos.')
flags.DEFINE_float(
    'eval_ratio', 0.1,
    'Fraction of input to set aside for eval set. Partition is randomly '
    'selected.')
flags.DEFINE_string('config', 'rnn-nade', 'Which config to use.')
flags.DEFINE_string(
    'log', 'INFO',
    'The threshold for what messages will be logged DEBUG, INFO, WARN, ERROR, '
    'or FATAL.')


def main(unused_argv):
  tf.logging.set_verbosity(FLAGS.log)

  pipeline_instance = pianoroll_pipeline.get_pipeline(
      min_steps=80,  # 5 measures
      max_steps=2048,
      eval_ratio=FLAGS.eval_ratio,
      config=pianoroll_rnn_nade_model.default_configs[FLAGS.config])

  input_dir = os.path.expanduser(FLAGS.input)
  output_dir = os.path.expanduser(FLAGS.output_dir)
  pipeline.run_pipeline_serial(
      pipeline_instance,
      pipeline.tf_record_iterator(input_dir, pipeline_instance.input_type),
      output_dir)


def console_entry_point():
  tf.disable_v2_behavior()
  tf.app.run(main)


if __name__ == '__main__':
  console_entry_point()
