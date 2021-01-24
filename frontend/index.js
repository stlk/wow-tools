import { Application } from 'stimulus';
import { Autocomplete } from 'stimulus-autocomplete';
import ToggleController from './controllers/toggle_controller';

const application = Application.start();
application.register('toggle', ToggleController);
application.register('autocomplete', Autocomplete);
